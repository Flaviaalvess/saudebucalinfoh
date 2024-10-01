from django.db import models

class pacientes(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Paciente")
    cpf = models.CharField(max_length=100, verbose_name="CPF")
    email = models.CharField(max_length=100, verbose_name="Email")
    telefone = models.CharField(max_length=11, verbose_name="Telefone")

    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.email}, {self.telefone}"

    class Meta:
        verbose_name = "paciente"
        verbose_name_plural = "pacientes"

class profissionais(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Dentista")
    cpf = models.CharField(max_length=100, verbose_name="CPF")
    email = models.CharField(max_length=100, verbose_name="Email")
    telefone = models.CharField(max_length=11, verbose_name="Telefone")

    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.email}, {self.telefone}"

    class Meta:
        verbose_name = "profissionais"
        verbose_name_plural = "profissionais"

class consulta(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Paciente")
    cpf = models.CharField(max_length=100, verbose_name="CPF")
    cep = models.CharField(max_length=100, verbose_name="Cep")
    email = models.CharField(max_length=100, verbose_name="Email")
    telefone = models.CharField(max_length=11, verbose_name="Telefone")

    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.cep}, {self.email}, {self.telefone}"

    class Meta:
        verbose_name = "consulta"
        verbose_name_plural = "consultas"

from django.db import models

class agendamento(models.Model):
    horario = models.CharField(max_length=100, verbose_name="Horário do Agendamento")
    data = models.DateField(verbose_name="Data do Agendamento")

    def __str__(self):
        return f"{self.horario}, {self.data}"

    class Meta:
        verbose_name = "agendamento"
        verbose_name_plural = "agendamentos"

class cuidado(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = "cuidado"
        verbose_name_plural = "cuidados"

class cuidado_especial(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome ")

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = "cuidado especial"
        verbose_name_plural = "cuidados especiais"

class orcamento(models.Model):
    cuidado = models.ForeignKey(cuidado, on_delete=models.CASCADE, verbose_name = "Nome" )
    cuidado_especial = models.ForeignKey(cuidado_especial, on_delete=models.CASCADE, verbose_name = "Nome" )

    def __str__(self):
        return f"{self.cuidado}, {self.cuidado_especial}"
    
    class Meta:
        verbose_name = "orcamento"
        verbose_name_plural = "orcamentos"

class HorarioDeAtendimento(models.Model):  # Classe renomeada para seguir a convenção
    horario = models.CharField(max_length=100, verbose_name="Horário do Atendimento")

    def __str__(self):
        return self.horario

    class Meta:
        verbose_name = "horário de atendimento"
        verbose_name_plural = "horários de atendimentos"

class contato(models.Model):
    telefone = models.CharField(max_length=11, verbose_name="Telefone de Contato")

    def __str__(self):
        return f"{self.telefone}"
    
    class Meta:
        verbose_name = "contato"
        verbose_name_plural = "contatos"
















