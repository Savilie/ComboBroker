from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from quiz_feedback.serializers import QuizSerializer, FeedbackSerializer
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from ComboBroker.settings import EMAIL_HOST_USER
# Create your views here.


class QuizView(APIView):

    @staticmethod
    def post(request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            number = f"""
            Номер телефона: {serializer.validated_data.get('number', 'Не указан')}
            """
            type = f"""
            Тип недвижимости: {serializer.validated_data.get('type', 'Не указан')}
            """
            price = f"""
            Цена: {serializer.validated_data.get('price', 'Не указана')} руб.
            """
            vznos = f"""
            Первоначальный взнос: {serializer.validated_data.get('vznos', 'Не указан')}
            """
            program = f"""
            Программа: {serializer.validated_data.get('program', 'Не указана')}
            """
            city = f"""
            Город: {serializer.validated_data.get('city', 'Не указан')}
            """
            subject = 'Заявка на консультацию'
            html_message = render_to_string('quiz/quiz.html', {'number': number, 'type': type, 'price': price,
                                                               'vznos': vznos, 'program': program, 'city': city})
            plain_message = strip_tags(html_message)

            try:
                send_mail(
                    subject,
                    plain_message,
                    '',
                    [EMAIL_HOST_USER],
                    html_message=html_message,
                    fail_silently=False,
                )
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackView(APIView):

    @staticmethod
    def post(request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            number = f"""
            Номер телефона: {serializer.validated_data.get('number', 'Не указан')}
            """
            theme = f"""
            Тема вопроса: {serializer.validated_data.get('theme', 'Не указана')}
            """
            messenger = f"""
            Предпочтительный мессенджер: {serializer.validated_data.get('messenger', 'Не указан')}
            """

            subject = 'Заявка на консультацию по форме обратной связи'
            html_message = render_to_string('feedback/feedback.html', {'number': number, 'theme': theme,
                                                               'messenger': messenger})
            plain_message = strip_tags(html_message)

            try:
                send_mail(
                    subject,
                    plain_message,
                    '',
                    [EMAIL_HOST_USER],
                    html_message=html_message,
                    fail_silently=False,
                )
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
