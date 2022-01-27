from django.db import models
from django.db.models.fields import EmailField


class Base(models.Model):
    nome_base = models.CharField(max_length=255)
    cidade_base = models.CharField(max_length=255)
    estado = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    cnpj = models.IntegerField(blank=True, null=True)
    regional = models.CharField(max_length=100, blank=True, null=True)
    faz_coleta = models.BooleanField(default=False)
    status_base = models.CharField(max_length=50, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_base or ''

    class Meta:
        verbose_name = "Base"
        verbose_name_plural = "Bases"

class Contatos(models.Model):
    nome_base = models.ForeignKey(Base, related_name='contatos', on_delete=models.CASCADE, default=True)
    nome_responsavel = models.CharField(max_length=255)
    telefone = models.CharField(max_length=100)
    email = models.EmailField()
    analista = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_base.nome_base or ''
    
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

class Abrangencia(models.Model):
    nome_base = models.ForeignKey(Base, on_delete=models.CASCADE, default=True)
    cidade = models.CharField(max_length=255)
    SLO = models.CharField(max_length=50)
    Faixa = models.CharField(max_length=50)

    def __str__(self):
        return self.cidade or ''

    class Meta:
        verbose_name = "Abrangência"
        verbose_name_plural = "Abrangência"

class Agendamentos(models.Model):
    nome_base = models.ForeignKey(Base, on_delete=models.CASCADE, default=True)
    data_hora = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    cancelado = models.BooleanField(default=False)
    tipo_agendamento = models.CharField(max_length=100)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_base.nome_base or ''
    
    class Meta:
        verbose_name = "Agendamento"
        
    



