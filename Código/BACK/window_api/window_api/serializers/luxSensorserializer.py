from rest_framework import serializers
from window_api.models.luxSensor import LuxSensor

class LuxSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuxSensor
        fields = '__all__'

