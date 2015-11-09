# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_auto_20150910_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='recebe_oferta',
            field=models.CharField(choices=[('N', 'NÃO'), ('S', 'SIM')], verbose_name='Recebe ofertas', max_length=1, default='N'),
            preserve_default=False,
        ),
    ]
