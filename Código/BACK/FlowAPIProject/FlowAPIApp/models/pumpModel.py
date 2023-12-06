from django.db import models

class PumpFlow(models.Model):
    litros_totais = models.FloatField()
    preco_por_litro = models.FloatField()