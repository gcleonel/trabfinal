# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_auto_20150823_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('saldo', models.IntegerField()),
                ('produto', models.ForeignKey(to='produtos.Produto')),
            ],
        ),
    ]
