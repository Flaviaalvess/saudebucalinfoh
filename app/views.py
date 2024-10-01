from django.shortcuts import render,redirect, get_object_or_404
from .models import*
from django.views import View

from django.contrib import messages
class indexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class pacienteView(View):
    def get(self, request, *args, **kwargs):
        paciente = pacientes.objects.all() 
        return render(request, 'pacientes.html', {'paciente':paciente})
    
class profissionaisView(View):
    def get(self, request, *args, **kwargs):
        profissionais = profissionais.objects.all() 
        return render(request, 'profissionais.html', {'profissionais':profissionais})
    
class consultaView(View):
    def get(self, request, *args, **kwargs):
        consultas = consulta.objects.all() 
        return render(request, 'consulta.html', {'consulta':consulta})
    
class agendamentoView(View):
    def get(self, request, *args, **kwargs):
        agendamentos = agendamento.objects.all() 
        return render(request, 'agendamento.html', {'agendamento':agendamento})
    
class cuidadoView(View):
    def get(self, request, *args, **kwargs):
        cuidados = cuidado.objects.all() 
        return render(request, 'cuidados.html', {'cuidado':cuidado})
    
class cuidado_especialView(View):
    def get(self, request, *args, **kwargs):
        cuidados_especiais = cuidado_especial.objects.all() 
        return render(request, 'cuidado_especial.html', {'cuidado_especial':cuidado_especial})
    
class orcamentoView(View):
    def get(self, request, *args, **kwargs):
        orcamentos = orcamento.objects.all() 
        return render(request, 'orcamento.html', {'orcamentos':orcamentos})
    
class HorarioView(View):  # Corrigido para seguir a convenção de nomenclatura
    def get(self, request, *args, **kwargs):
        horarios_de_atendimentos = HorarioDeAtendimento.objects.all()  # Corrigido para usar a classe correta
        return render(request, 'horario.html', {'horarios_de_atendimento': horarios_de_atendimentos})  # Corrigido o nome da variável
    
class contatoView(View):
    def get(self, request, *args, **kwargs):
        contatos = contato.objects.all() 
        return render(request, 'contato.html', {'contatos':contatos})
    
    

    
    
    

    

    


# Create your views here.
