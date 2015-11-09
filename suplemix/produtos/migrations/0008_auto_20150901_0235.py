# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_auto_20150824_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='valor_compra',
            field=models.DecimalField(help_text='Volor que foi comprado.', verbose_name='valor de compra R$', decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valor_venda',
            field=models.DecimalField(help_text='Volor que será vendido.', verbose_name='valor de venda R$', decimal_places=2, max_digits=5),
        ),
    ]
