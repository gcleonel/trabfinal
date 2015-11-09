# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_auto_20150926_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='produto',
            name='subcategoria',
            field=models.ForeignKey(to='produtos.Subcategoria', default=0),
            preserve_default=False,
        ),
    ]
