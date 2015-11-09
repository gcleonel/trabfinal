# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20150908_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rua',
            field=models.CharField(verbose_name='Rua', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_endereco',
            field=models.CharField(max_length=1, choices=[('0', 'Apartamento'), ('1', 'Casa'), ('2', 'Comercial'), ('3', 'Outros')]),
        ),
    ]
