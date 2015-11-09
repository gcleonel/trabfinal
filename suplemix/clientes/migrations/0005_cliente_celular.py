# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_cliente_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='celular',
            field=models.CharField(max_length=14, verbose_name='Telefone', default=1, help_text='(99)99999-9999'),
            preserve_default=False,
        ),
    ]
