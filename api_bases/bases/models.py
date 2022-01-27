from django.db import models

class Bases(models.Model):
    id_base = models.AutoField(primary_key=True)
    nome_base = models.CharField(max_length=80, blank=True, null=True)
    status_base = models.CharField(max_length=50, blank=True, null=True)
    prazo_entrega = models.CharField(max_length=20, blank=True, null=True)
    volume_dia = models.IntegerField(blank=True, null=True)
    faz_coleta = models.BooleanField(default=False)
    cnpj = models.IntegerField(blank=True, null=True)
    nome_proprietario_base = models.CharField(max_length=100, blank=True, null=True)
    nome_gestor_base = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.IntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    numero_endereco = models.IntegerField(blank=True, null=True)
    bairro_endereco = models.CharField(max_length=60, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    regional = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    analista_responsavel = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bases'