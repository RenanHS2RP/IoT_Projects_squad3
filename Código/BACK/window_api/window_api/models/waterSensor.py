from django.db import models

class WaterSensor(models.Model):
    is_raining = models.BooleanField()