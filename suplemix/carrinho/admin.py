from django.contrib import admin
from suplemix.carrinho.models import Carrinho, ItemCarrinho

# Register your models here.

@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
	list_display = ('id','produto', 'quantidade', 'carrinho',)
	search_fields = ('id',)

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
	list_display = ('id','itens')
	search_fields = ('id',)