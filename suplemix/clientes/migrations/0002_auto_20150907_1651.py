# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='user',
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(unique=True, max_length=50, default=datetime.datetime(2015, 9, 7, 16, 50, 49, 421068, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default='admin', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='senha',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(default='admin', max_length=100),
            preserve_default=False,
        ),
    ]
