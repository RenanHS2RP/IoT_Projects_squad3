# models.py
from django.db import models

class WeatherForecast(models.Model):
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    date = models.DateTimeField()
    date_br = models.DateTimeField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    precipitation = models.FloatField()
    wind_velocity = models.FloatField()
    wind_direction = models.CharField(max_length=255)
    wind_direction_degrees = models.FloatField(null=True)
    wind_gust = models.FloatField()
    temperature = models.FloatField()

    def __str__(self):
        return f"{self.city_name} - {self.date}"
