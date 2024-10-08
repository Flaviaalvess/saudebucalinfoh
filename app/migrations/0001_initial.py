# Generated by Django 5.1 on 2024-09-23 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(max_length=100, verbose_name='Horário do Agendamento')),
                ('data', models.DateField(verbose_name='Data do Agendamento')),
            ],
            options={
                'verbose_name': 'agendamento',
                'verbose_name_plural': 'agendamentos',
            },
        ),
        migrations.CreateModel(
            name='consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Paciente')),
                ('cpf', models.CharField(max_length=100, verbose_name='CPF')),
                ('cep', models.CharField(max_length=100, verbose_name='Cep')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'consulta',
                'verbose_name_plural': 'consultas',
            },
        ),
        migrations.CreateModel(
            name='contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone de Contato')),
            ],
            options={
                'verbose_name': 'contato',
                'verbose_name_plural': 'contatos',
            },
        ),
        migrations.CreateModel(
            name='cuidado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'cuidado',
                'verbose_name_plural': 'cuidados',
            },
        ),
        migrations.CreateModel(
            name='cuidado_especial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome ')),
            ],
            options={
                'verbose_name': 'cuidado especial',
                'verbose_name_plural': 'cuidados especiais',
            },
        ),
        migrations.CreateModel(
            name='dentista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Dentista')),
                ('cpf', models.CharField(max_length=100, verbose_name='CPF')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'dentista',
                'verbose_name_plural': 'dentistas',
            },
        ),
        migrations.CreateModel(
            name='horariodeatendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(max_length=100, verbose_name='Horário do Atendimento')),
            ],
            options={
                'verbose_name': 'horário de atendimento',
                'verbose_name_plural': 'horários de atendimentos',
            },
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Paciente')),
                ('cpf', models.CharField(max_length=100, verbose_name='CPF')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'paciente',
                'verbose_name_plural': 'pacientes',
            },
        ),
        migrations.CreateModel(
            name='orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuidado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cuidado', verbose_name='Nome')),
                ('cuidado_especial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cuidado_especial', verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'orcamento',
                'verbose_name_plural': 'orcamentos',
            },
        ),
    ]
