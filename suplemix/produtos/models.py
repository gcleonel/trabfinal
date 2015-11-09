# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Categoria(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome


class Subcategoria(models.Model):
	descricao = models.CharField(max_length=100)
	categoria = models.ForeignKey(Categoria)

	def __str__(self):
		return self.descricao


class Produto(models.Model):
	IS_PROMOCAO_CHOICES = (('N', 'NÃO'),('S', 'SIM'),)
	descricaoreduzida = models.CharField(u'Descrição Reduzida',max_length=255)
	descricaocompleta = models.CharField(u'Descrição Completa', max_length=255)
	resumo 			  = models.CharField(u'Resumo', max_length=255)
	ingredientes      = models.TextField(u'Ingredientes')
	valor_compra      = models.DecimalField(u'valor de compra R$', max_digits=5, decimal_places=2, help_text='Volor que foi comprado.');
	valor_venda       = models.DecimalField(u'valor de venda R$', max_digits=5, decimal_places=2, help_text='Volor que será vendido.');
	subcategoria      = models.ForeignKey(Subcategoria)
	estoque           = models.IntegerField()
	foto              = models.ImageField(upload_to="images/prodthumbs/")
	is_promocao       = models.CharField(max_length=1, choices=IS_PROMOCAO_CHOICES)
	valor_promocao    = models.DecimalField(u'valor promocional R$', max_digits=5, decimal_places=2, help_text='Volor que será vendido quando for promocional.');

	def __str__(self):
		return self.descricaoreduzida

	def get_preco(self):
		if self.is_promocao == 'N':
			return self.valor_venda
		else:
			return self.valor_promocao



class Imagem(models.Model):
	descricao = models.CharField(max_length=100)
	link      = models.CharField(max_length=100)
	produto   = models.ForeignKey(Produto)
	arquivo   = models.ImageField(upload_to=u'imgs/produto')

	def __str__(self):
		return self.descricao