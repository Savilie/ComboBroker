# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from external.serializers import INNSerializer
from ComboBroker.settings import EFRSB_LOGIN, EFRSB_PASSWORD


class ExternalAPIDataView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def authorize():
        try:
            # Делать запрос к внешнему сервису
            external_api_url = 'https://bank-publications-demo.fedresurs.ru/v1/auth/'
            json = {"login": EFRSB_LOGIN, "password": EFRSB_PASSWORD}
            response = requests.post(external_api_url, json=json)

            # Проверить статус ответа
            if response.status_code == 200:
                # Обработать и вернуть данные
                data = response.json()
                return data
            else:
                # Вернуть ошибку, если что-то пошло не так
                return Response({'error': 'Failed to fetch data from external API'}, status=response.status_code)

        except requests.RequestException as e:
            # Обрабатывать исключения, если запрос не удался
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        if request.user.is_authenticated:
            try:
                jwt = self.authorize().get('jwt')
                headers = {
                    "Authorization": f"Bearer {jwt}",
                }
                inn_serializer = INNSerializer(data=request.data)
                if inn_serializer.is_valid():
                    inn = request.data.get('inn')
                    data = requests.get(
                        f"https://bank-publications-demo.fedresurs.ru/v1/bankrupts/?type=Person&inn={inn}&limit=500&offset=0",
                        headers=headers).json()
                    fns_data = requests.get(f"https://gosnalogi.ru/ajax/taxes_inn?inn={inn}").json()
                    data.update(fns_data)
                    return Response(data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
