# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('arquivo', models.ImageField(upload_to='imgs/produto')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('descricaoreduzida', models.CharField(max_length=255, verbose_name='Descrição Reduzida')),
                ('descricaocompleta', models.CharField(max_length=255, verbose_name='Descrição Completa')),
                ('valor_compra', models.FloatField(verbose_name='Valor de Compra')),
                ('valor_venda', models.FloatField(verbose_name='Valor de Venda')),
                ('categoria', models.ForeignKey(to='produtos.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='imagem',
            name='produto',
            field=models.ForeignKey(to='produtos.Produto'),
        ),
    ]
