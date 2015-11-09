# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20150907_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tipo_endereco',
            field=models.CharField(choices=[(0, 'Apartamento'), (1, 'Casa'), (2, 'Comercial'), (3, 'Outros')], max_length=1, default=1),
            preserve_default=False,
        ),
    ]
