# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_cliente_tipo_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='bairro',
            field=models.CharField(max_length=100, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(max_length=14, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(unique=True, max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, help_text='*'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='info_referencia',
            field=models.CharField(max_length=100, verbose_name='Informaçoes de referência'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rua',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='senha',
            field=models.CharField(default=None, max_length=50, verbose_name='Senha'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(max_length=100, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=14, verbose_name='Telefone'),
        ),
    ]
