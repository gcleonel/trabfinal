# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0008_auto_20150901_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('total', models.DecimalField(default=0.0, max_digits=100, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('quantidade', models.IntegerField(default=1)),
                ('dataRegistro', models.DateTimeField(auto_now_add=True)),
                ('carrinho', models.ForeignKey(to='carrinho.Carrinho', null=True, blank=True)),
                ('produto', models.ForeignKey(to='produtos.Produto')),
            ],
        ),
    ]
