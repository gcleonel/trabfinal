# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_cliente_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='bairro',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='info_referencia',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='rua',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(verbose_name='Celular', help_text='(99)99999-9999', max_length=14),
        ),
    ]
