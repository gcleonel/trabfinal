# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0008_auto_20150901_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(to='produtos.Categoria')),
            ],
        ),
        migrations.AlterField(
            model_name='produto',
            name='ingredientes',
            field=models.TextField(verbose_name='Ingredientes'),
        ),
    ]
