import requests
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from window_api.utils.forecast import ClimatempoAPI
from window_api.serializers.weatherForecastSerializer import WeatherForecastSerializer
from window_api.models.weatherForecast import WeatherForecast
from rest_framework.decorators import api_view

class WeatherForecastAPIView(ModelViewSet):
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer

    def create(self, request, *args, **kwargs):
        try:
            raw_data = request.data

            climatempo_instance = ClimatempoAPI(token="055ebe3b48afc896373ca3b61458542b")
            city_id = climatempo_instance.get_city_id(raw_data['city_name'])
            forecast_data = climatempo_instance.get_forecast_72_hours(city_id)
            processed_data = climatempo_instance.process_forecast_data(forecast_data)

            # Enviando para o ThingsBoard
            thingsboard = ThingsBoard('climatempo')

            # Iterando sobre cada objeto no JSON e enviando para o ThingsBoard
            for data_point in processed_data:
                thingsboard.post_telemetry(data_point)

                # Salvando cada objeto no banco de dados
                serializer = self.serializer_class(data=data_point)
                serializer.is_valid(raise_exception=True)
                serializer.save()

            return Response({"success": "Dados de previsão do tempo processados com sucesso.", "data": processed_data}, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            return Response({"error": "Validation error", "detail": e.args}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": "Erro ao processar dados de previsão do tempo.", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ThingsBoard:
    def __init__(self, token):
        self.token = token

    def post_telemetry(self, telemetry_list):
        # Endpoint do ThingsBoard local
        url = f'http://127.0.0.1:8089/api/v1/{self.token}/telemetry'
        headers = {'Content-Type': 'application/json'}

        try:
            for telemetry in telemetry_list:
                telemetry['date'] = telemetry['date'].isoformat()
                telemetry['date_br'] = telemetry['date_br'].isoformat()

                # Enviando cada objeto separadamente para o endpoint do ThingsBoard
                # response = requests.post(url, json=[telemetry], headers=headers)

                # Verificar a resposta do ThingsBoard
                # response.raise_for_status()

            telemetry = {
                "payload": telemetry_list
            }

            response = requests.post(url, json=telemetry, headers=headers)
            response.raise_for_status()

            print('sucesso')
            return HttpResponse({"message": "Sucesso"})

        except Exception as e:
            print("detail", e.args)
            return HttpResponse({"message": "Erro", "detail": e.args})

