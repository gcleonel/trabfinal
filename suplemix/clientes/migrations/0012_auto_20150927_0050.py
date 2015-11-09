# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_cliente_recebe_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='data_atualizacao',
            field=models.DateField(auto_now_add=True, verbose_name='Date', default=datetime.datetime(2015, 9, 27, 0, 50, 2, 702682, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, verbose_name='Date', default=datetime.datetime(2015, 9, 27, 0, 50, 13, 495126, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
