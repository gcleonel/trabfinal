# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0010_auto_20150926_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='is_promocao',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'NÃO'), ('S', 'SIM')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='valor_promocao',
            field=models.DecimalField(help_text='Volor que será vendido quando for promocional.', decimal_places=2, verbose_name='valor promocional R$', default=0.0, max_digits=5),
            preserve_default=False,
        ),
    ]
