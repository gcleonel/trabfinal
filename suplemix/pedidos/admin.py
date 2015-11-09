from django.contrib import admin
from suplemix.pedidos.models import Pedido

# Register your models here.
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
	list_display = ( 'cliente', 'qnt_itens', 'total', 'cep', 'rua', 'numero', 'bairro', 'cidade', 'uf', 'status',)
	search_fields = ('id',)