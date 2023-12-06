from django.db import models

class FlowSensor(models.Model):
    tempo_operacao = models.DateTimeField()
    litros_totais = models.FloatField()
    litros_por_minuto = models.FloatField()