from django.db import models
from suplemix.produtos.models import Produto

# Create your models here.

class ItemCarrinho(models.Model):
	produto  	 = models.ForeignKey(Produto)
	carrinho 	 = models.ForeignKey('Carrinho', null=False, blank=True)
	quantidade 	 = models.IntegerField(default=1)
	dataRegistro = models.DateTimeField(auto_now_add=True, auto_now=False)
	total 		 = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

	def __str__(self):
		try:
			return str(self.id)
		except:
			return str(self.produto.descricaoreduzida)

class Carrinho(models.Model):
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	itens = models.IntegerField(default=0)
	email_cliente = models.CharField(max_length=100)
	#id_session   = models.CharField(max_length=100)
	
	def __str__(self):
		return str(self.id)
