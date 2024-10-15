from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.cache import cache
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

from users.models import CustomUser
from users.serializers import PasswordResetRequestSerializer, PasswordResetConfirmSerializer, CustomUserSerializer

from ComboBroker.settings import EMAIL_HOST_USER

# Create your views here.

class CustomUserAPIView(APIView):

    @staticmethod
    def get(request):
        if not request.user.is_authenticated:
            user = CustomUser.objects.get(id=request.user.id)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        if request.user.is_superuser:

            users = CustomUser.objects.all()
            serializer = CustomUserSerializer(users, many=True)

            return Response(serializer.data)
        return Response(str(Exception))

    @staticmethod
    def post(request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            message = 'User created, verification email sent.' if not user.is_authenticated else 'Verification email sent again.'
            return Response({'detail': message}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        id = request.query_params.get('id', None)
        if id:
            user = CustomUser.objects.get(id=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class VerifyEmailAPIView(APIView):
    @staticmethod
    def post(request):
        email = request.data.get('email')
        code = request.data.get('code')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        cached_code = cache.get(f"email_verification_{user.email}")

        if cached_code and cached_code == code:
            user.is_authenticated = True
            user.save()
            cache.delete(f"email_verification_{user.email}")  # Удаляем запись после успешной верификации.
            return Response({'detail': 'Email verified successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid or expired verification code.'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestView(APIView):

    @staticmethod
    def post(request):

        serializer = PasswordResetRequestSerializer(data=request.data)

        if serializer.is_valid():

            email = serializer.validated_data['email']
            sender = EMAIL_HOST_USER
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({"detail": "User with this email does not exist."},
                                status=status.HTTP_400_BAD_REQUEST)

            token = default_token_generator.make_token(user)

            send_mail(
                'Password Reset',
                f'Use this link to reset your password: localhost:8000/password-confirm?token={token}&&uid={user.id}',
                sender,
                [email],
                fail_silently=False,
            )
            return Response({"detail": "Password reset email sent."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):

        serializer = PasswordResetConfirmSerializer(data=request.data)

        if serializer.is_valid():

            token = request.query_params.get('token')
            password = serializer.validated_data['password']
            try:
                uid = request.query_params.get('uid')
                user = CustomUser.objects.get(id=uid)
                if default_token_generator.check_token(user, token):
                    user.set_password(password)
                    user.save()
                    return Response({"detail": "Password has been reset."}, status=status.HTTP_200_OK)
                else:
                    return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

            except (CustomUser.DoesNotExist, ValueError):
                return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)