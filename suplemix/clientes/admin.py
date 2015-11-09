from django.contrib import admin
from suplemix.clientes.models import Cliente

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome','sobrenome', 'email', 'sexo', 'cidade', 'estado', 'recebe_oferta','data_cadastro')
	search_fields = ('id',)