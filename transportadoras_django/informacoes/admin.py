from django.contrib import admin
from . import models

class ContatosInLine(admin.TabularInline):
    model = models.Contatos
    extra = 0

class AbrangenciaInLine(admin.TabularInline):
    model = models.Abrangencia
    extra = 0

class AgendamentosInLine(admin.TabularInline):
    model = models.Agendamentos
    extra = 0
    
class BaseAdmin(admin.ModelAdmin):
    inlines = [
        ContatosInLine,
        AbrangenciaInLine,
        AgendamentosInLine
    ]

admin.site.register(models.Base, BaseAdmin)
admin.site.register(models.Contatos)
admin.site.register(models.Abrangencia)
admin.site.register(models.Agendamentos)
