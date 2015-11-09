# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_auto_20151016_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='email_cliente',
            field=models.CharField(max_length=50),
        ),
    ]
