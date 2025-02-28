from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from quiz_feedback.serializers import QuizSerializer, FeedbackSerializer
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from ComboBroker.settings import EMAIL_HOST_USER

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes, OpenApiExample, OpenApiResponse
# Create your views here.


class QuizView(APIView):

    @staticmethod
    @extend_schema(
        description="""Accepts JSON with fields: number (phone number), type (property type), price (price),
        vznos (down payment), program (program), city (city).
        Sends a letter to the specified email with the data from the request.""",
    request={
            'application/json': {
                'schema': {
                  'type': 'object',
                  'properties': {
                      'number': {'type': 'string', 'description': 'Номер телефона'},
                      'type': {'type': 'string', 'description': 'Тип недвижимости'},
                      'price': {'type': 'integer', 'description': 'Цена'},
                      'vznos': {'type': 'integer', 'description': 'Первоначальный взнос'},
                      'program': {'type': 'string', 'description': 'Программа'},
                      'city': {'type': 'string', 'description': 'Город'}
                   },
                  'required': ['number', 'type', 'price', 'vznos', 'program', 'city']
                },
                'example': {
                  "number": "+79001234567",
                  "type": "Квартира",
                  "price": 5000000,
                  "vznos": 1000000,
                  "program": "Семейная ипотека",
                  "city": "Москва"
                  }
            }
        },
    responses={
        200: OpenApiResponse(
            description="Заявка успешно отправлена. Email отправлен.",
            response=QuizSerializer,
            examples=[
                OpenApiExample(
                    'Success Response Example',
                    value={
                        "number": "+79001234567",
                        "type": "Квартира",
                        "price": 5000000,
                        "vznos": 1000000,
                        "program": "Семейная ипотека",
                        "city": "Москва"
                    }
                )
             ]
        )
    },

    )
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
    @extend_schema(
        description="""Accepts JSON with fields: number (phone number), theme (question theme), messenger (preferred messenger).
        Sends a letter to the specified email with the data from the request.""",
    request={
            'application/json': {
                'schema': {
                  'type': 'object',
                  'properties': {
                      'number': {'type': 'string', 'description': 'Номер телефона'},
                      'theme': {'type': 'string', 'description': 'Тема вопроса'},
                      'messenger': {'type': 'string', 'description': 'Предпочтительный мессенджер'}
                   },
                  'required': ['number', 'theme', 'messenger']
                },
                'example': {
                  "number": "+79001234567",
                  "theme": "Хочу получить кредит, но не знаю как",
                  "messenger": "Telegram"
                  }
            }
        }
    )
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
