import requests
import json
from django.http import JsonResponse

class ThingsBoard:
    def __init__(self, token):
        self.token = token

    def post_telemetry(self, telemetry):
        url = f'http://127.0.0.1:8080/api/v1/{self.token}/telemetry'
        try:
            response = requests.post(url, json=telemetry)
            response.raise_for_status()
            return JsonResponse({"message": "Sucess"})
        except Exception as e:
            return e
        
   