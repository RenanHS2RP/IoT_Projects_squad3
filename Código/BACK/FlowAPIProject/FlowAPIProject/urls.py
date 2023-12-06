from rest_framework import routers
from django.urls import path, include
from FlowAPIApp.views.pumpView import PumpView
from FlowAPIApp.views.sensorView import FlowView


router = routers.DefaultRouter()
router.register(r'pump', PumpView)
router.register(r'sensor', FlowView)

urlpatterns = [
    path('', include(router.urls)),
]
