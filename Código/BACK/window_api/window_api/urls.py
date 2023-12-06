from django.urls import path, include
from window_api.views.luxSensorview import LuxSensorView
from window_api.views.waterSensorview import WaterSensorView
from rest_framework import routers
from window_api.views.forecastView import WeatherForecastAPIView

router = routers.DefaultRouter()
router.register('luminosidade', LuxSensorView)
router.register('chuva', WaterSensorView)
router.register('previsao', WeatherForecastAPIView)

urlpatterns = [
    path('', include(router.urls))
]
