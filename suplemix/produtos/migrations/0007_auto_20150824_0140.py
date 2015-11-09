# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_auto_20150824_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.ImageField(upload_to='images/prodthumbs/'),
        ),
    ]
