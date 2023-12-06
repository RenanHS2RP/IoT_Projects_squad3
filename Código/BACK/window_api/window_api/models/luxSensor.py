from django.db import models

class LuxSensor(models.Model):
    lux = models.IntegerField()
