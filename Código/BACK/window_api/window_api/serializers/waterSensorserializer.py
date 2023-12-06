from rest_framework import serializers
from window_api.models.waterSensor import WaterSensor

class WaterSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterSensor
        fields = '__all__'

