# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0003_itemcarrinho_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrinho',
            name='carrinho',
            field=models.ForeignKey(to='carrinho.Carrinho', blank=True),
        ),
    ]
