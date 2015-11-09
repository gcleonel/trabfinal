from django.contrib import admin
from suplemix.produtos.models import Produto, Categoria, Subcategoria, Imagem

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nome',)
	search_fields = ('nome',)

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
	list_display = ('id','descricao')
	search_fields = ('descricao',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('descricaoreduzida','valor_compra', 'valor_venda', 'subcategoria','estoque','is_promocao')
	search_fields = ('descricaoreduzida',)


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
	list_display = ('id','produto','descricao','arquivo',)
	search_fields = ('produto',)
