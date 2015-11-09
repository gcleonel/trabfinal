from django.db import models
from suplemix.produtos.models import Produto
from suplemix.clientes.models import Cliente

# Create your models here.

class Pedido(models.Model):
	data_pedido      = models.DateTimeField(auto_now_add=True)
	data_atualizacao = models.DateTimeField(auto_now_add=True, auto_now=False)
	cliente          = models.ForeignKey(Cliente)
	email_cliente    = models.CharField(max_length=50)
	qnt_itens        = models.IntegerField(default=0)
	total 		     = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	cep    			 = models.CharField(max_length=100)
	rua              = models.CharField(max_length=100)
	numero           = models.CharField(max_length=20)
	complemento      = models.CharField(max_length=100)
	bairro           = models.CharField(max_length=100)
	cidade           = models.CharField(max_length=100)
	uf               = models.CharField(max_length=2)
	status           = models.CharField(max_length=1)

	def __str__(self):
		return str(self.id)


class ItemPedido(models.Model):
	pedido   = models.ForeignKey(Pedido)
	produto  = models.ForeignKey(Produto)
	qnt      = models.IntegerField(default=0)
	subtotal = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

	def __str__(self):
		return str(self.id)