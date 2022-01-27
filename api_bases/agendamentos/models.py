from django.db import models
from bases.models import Bases

class Agendamentos(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    data_hora = models.DateTimeField(blank=False, null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    cancelado = models.BooleanField(default=False)
    tipo_agendamento = models.CharField(max_length=100, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    id_base = models.ForeignKey(Bases, on_delete=models.CASCADE, related_name='agendamentos', blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'agendamentos'
        unique_together = ('data_hora', 'id_base')

