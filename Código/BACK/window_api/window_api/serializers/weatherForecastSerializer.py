from rest_framework import serializers
from window_api.models.weatherForecast import WeatherForecast

class WeatherForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        fields = '__all__'