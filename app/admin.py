from django.contrib import admin
from .models import*
from django.contrib import admin
admin.site.register(pacientes)
admin.site.register(profissionais)
admin.site.register(consulta)
admin.site.register(agendamento)
admin.site.register(cuidado)
admin.site.register(cuidado_especial)
admin.site.register(orcamento)
admin.site.register(HorarioDeAtendimento)
admin.site.register(contato)

# Register your models here.
