# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_carrinho_itens'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcarrinho',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
