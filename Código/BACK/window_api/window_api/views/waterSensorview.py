import requests
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from window_api.models.waterSensor import WaterSensor
from window_api.serializers.waterSensorserializer import WaterSensorSerializer

class WaterSensorView(viewsets.ModelViewSet):
    queryset = WaterSensor.objects.all()
    serializer_class = WaterSensorSerializer

    # Assuming ThingsBoard
    thingsboard_url = 'http://127.0.0.1:8089/api/v1/device/telemetry'
    thingsboard_token = 'device' 

    def send_water_telemetry(self, telemetry_data):
        headers = {
            'Content-Type': 'application/json',
            'X-Authorization': f'Token {self.thingsboard_token}',
        }

        try:
            response = requests.post(self.thingsboard_url, json=telemetry_data, headers=headers)
            # Handle the response if needed
            print(response.text)
        except Exception as e:
            # Handle the exception if needed
            print(e)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Assuming the serializer saves the data to WaterSensor model
        # Remove the reference to the 'temperature' field
        water_telemetry_data = {"is_raining": serializer.data["is_raining"]}

        # Send Water telemetry data to the new ThingsBoard endpoint
        self.send_water_telemetry(water_telemetry_data)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
