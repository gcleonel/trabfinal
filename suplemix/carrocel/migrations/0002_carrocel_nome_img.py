# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrocel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrocel',
            name='nome_img',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
