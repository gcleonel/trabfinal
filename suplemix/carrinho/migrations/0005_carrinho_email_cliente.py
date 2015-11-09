# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0004_auto_20150907_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='email_cliente',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
    ]
