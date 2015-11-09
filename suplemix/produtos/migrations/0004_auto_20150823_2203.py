# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_estoque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoque',
            name='produto',
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Estoque',
        ),
    ]
