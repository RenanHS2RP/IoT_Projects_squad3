import requests
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from window_api.models.luxSensor import LuxSensor
from window_api.serializers.luxSensorserializer import LuxSensorSerializer

class LuxSensorView(viewsets.ModelViewSet):
    queryset = LuxSensor.objects.all()
    serializer_class = LuxSensorSerializer

    # Assuming ThingsBoard URL is http://127.0.0.1:8089/api/v1/device/telemetry
    thingsboard_url = 'http://127.0.0.1:8089/api/v1/device/telemetry'
    thingsboard_token = 'device'  # Replace with your actual token

    def send_lux_telemetry(self, telemetry_data):
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

        # Assuming the serializer saves the data to LuxSensor model
        lux_telemetry_data = {"lux": serializer.data["lux"]}

        # Send Lux telemetry data to the new ThingsBoard endpoint
        self.send_lux_telemetry(lux_telemetry_data)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
