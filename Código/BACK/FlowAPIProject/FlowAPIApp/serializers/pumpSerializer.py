from rest_framework import serializers
from FlowAPIApp.models.pumpModel import PumpFlow

class PumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PumpFlow
        fields = '__all__'