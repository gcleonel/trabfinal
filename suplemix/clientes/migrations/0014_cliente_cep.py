# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0013_auto_20151004_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cep',
            field=models.CharField(default='', verbose_name='Cep', max_length=50),
            preserve_default=False,
        ),
    ]
