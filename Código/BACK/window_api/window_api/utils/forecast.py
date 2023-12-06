import requests
from datetime import datetime
from window_api.models.weatherForecast import WeatherForecast

class ClimatempoAPI:
    def __init__(self, token):
        self.token = token

    def get_current_weather(self, city_id):
        url = f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{city_id}/current?token={self.token}"
        response = requests.get(url)
        return response.json()

    def get_forecast_72_hours(self, city_id):
        url = f"http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{city_id}/hours/72?token={self.token}"
        response = requests.get(url)
        return response.json()

    @staticmethod
    def process_forecast_data(raw_data):
        processed_data_list = []

        base_data = {
            'city_id': raw_data['id'],
            'city_name': raw_data['name'],
            'state': raw_data['state'],
            'country': raw_data['country'],
        }

        forecasts = raw_data['data']

        for forecast_data in forecasts:
            processed_data = base_data.copy()

            processed_data['date'] = datetime.strptime(forecast_data['date'], "%Y-%m-%d %H:%M:%S")
            processed_data['date_br'] = datetime.strptime(forecast_data['date_br'], "%d/%m/%Y %H:%M:%S")
            processed_data['humidity'] = forecast_data['humidity']['humidity']
            processed_data['pressure'] = forecast_data['pressure']['pressure']
            processed_data['precipitation'] = forecast_data['rain']['precipitation']
            processed_data['wind_velocity'] = forecast_data['wind']['velocity']
            processed_data['wind_direction'] = forecast_data['wind']['direction']
            processed_data['wind_direction_degrees'] = forecast_data['wind'].get('direction_degrees', None)
            processed_data['wind_gust'] = forecast_data['wind']['gust']
            processed_data['temperature'] = forecast_data['temperature']['temperature']

            processed_data_list.append(processed_data)

            if processed_data['wind_direction_degrees'] is not None:
                WeatherForecast.objects.create(**processed_data)

        return processed_data_list

    def get_city_id(self, city_name):
        url = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={city_name}&token={self.token}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data:
                first_city = data[0]
                return first_city.get('id') if first_city else None

        return None

    def link_city_to_token(self, city_id):
        url = f"http://apiadvisor.climatempo.com.br/api-manager/user-token/{self.token}/locales"
        payload = f"localeId[]={city_id}"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, headers=headers, data=payload)
        return response.status_code
