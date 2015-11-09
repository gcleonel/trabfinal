# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20150823_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='foto',
            field=models.ImageField(upload_to='produto/img/', default=2),
            preserve_default=False,
        ),
    ]
