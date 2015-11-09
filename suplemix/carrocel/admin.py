from django.contrib import admin
from suplemix.carrocel.models import Carrocel

# Register your models here.

@admin.register(Carrocel)
class CarrocelAdmin(admin.ModelAdmin):
	list_display = ('id','nome_img','imagem')
	search_fields = ('nome_img',)

