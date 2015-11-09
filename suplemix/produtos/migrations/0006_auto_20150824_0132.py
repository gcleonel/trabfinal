# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_produto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.ImageField(upload_to='img'),
        ),
    ]
