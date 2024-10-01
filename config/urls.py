from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('pacientes/', pacienteView.as_view(), name='paciente'),
    path('profissionais/', profissionaisView.as_view(), name='profissionais'),
    path('consulta/', consultaView.as_view(), name='consulta'),
    path('agendamento/', agendamentoView.as_view(), name='agendamento'),
    path('cuidados/', cuidadoView.as_view(), name='cuidado'),
    path('cuidado_especial/', cuidado_especialView.as_view(), name='cuidado_especial'),
    path('orcamento/', orcamentoView.as_view(), name='orcamento'),
    path('horario_de_atendimento/', HorarioView.as_view(), name='horario'),
    path('contato/', contatoView.as_view(), name='contato'),

]