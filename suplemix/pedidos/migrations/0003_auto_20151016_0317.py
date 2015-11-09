# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20151005_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='email_cliente',
            field=models.CharField(max_length=50, default='', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
