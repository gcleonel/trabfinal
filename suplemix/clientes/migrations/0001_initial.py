# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('telefone', models.CharField(max_length=14, help_text='(99)99999-9999', verbose_name='Telefone')),
                ('sexo', models.CharField(max_length=1)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
