# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0013_auto_20151004_0417'),
        ('produtos', '0010_auto_20150926_2338'),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('qnt', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(default=0.0, max_digits=100, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='bairro',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='cep',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='cidade',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(to='clientes.Cliente', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='complemento',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='data_atualizacao',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2015, 9, 27, 0, 50, 2, 702682, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='numero',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='qnt_itens',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='rua',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(default='P', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(default=0.0, max_digits=100, decimal_places=2),
        ),
        migrations.AddField(
            model_name='pedido',
            name='uf',
            field=models.CharField(default='MA', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(to='pedidos.Pedido'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='produto',
            field=models.ForeignKey(to='produtos.Produto'),
        ),
    ]
