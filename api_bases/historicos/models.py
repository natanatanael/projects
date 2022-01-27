from django.db import models
from django.db.models.deletion import CASCADE
from agendamentos.models import Agendamentos

class Historicos(models.Model):
    id_historico = models.AutoField(primary_key=True)
    data = models.DateTimeField(auto_now_add=True)
    pendencias = models.CharField(max_length=100, blank=True, null=True)
    performance_anterior = models.IntegerField(blank=True, null=True)
    pontos_atencao = models.CharField(max_length=200, blank=True, null=True)
    conclusao = models.TextField(blank=True, null=True)
    id_agendamento = models.ForeignKey(Agendamentos, related_name='historicos', on_delete=CASCADE, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'historicos'
        

