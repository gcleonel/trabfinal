# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='ingredientes',
            field=models.CharField(verbose_name='Ingredientes', max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='resumo',
            field=models.CharField(verbose_name='Resumo', max_length=255, default=''),
            preserve_default=False,
        ),
    ]
