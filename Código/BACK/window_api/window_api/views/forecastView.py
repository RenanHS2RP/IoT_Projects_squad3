from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from window_api.utils.forecast import ClimatempoAPI
from window_api.utils.thingsBoard import ThingsBoard
from window_api.serializers.weatherForecastSerializer import WeatherForecastSerializer
from window_api.models.weatherForecast import WeatherForecast
from rest_framework.decorators import api_view
import requests


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

            #Enviando para o ThingsBoard
            thingsboard = ThingsBoard('climatempo')
            thingsboard.post_telemetry(processed_data)

            serializer = self.serializer_class(data=processed_data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            return Response({"success": "Dados de previsão do tempo processados com sucesso.", "data": processed_data}, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            return Response({"error": "Validation error", "detail": e.args}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": "Erro ao processar dados de previsão do tempo.", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
