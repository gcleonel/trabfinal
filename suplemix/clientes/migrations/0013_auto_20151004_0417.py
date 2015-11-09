# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0012_auto_20150927_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_atualizacao',
            field=models.DateField(verbose_name='Data Atualização', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_cadastro',
            field=models.DateField(verbose_name='Data Cadastro', auto_now_add=True),
        ),
    ]
