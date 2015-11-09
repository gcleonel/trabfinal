from django import forms
from suplemix.clientes.models import Cliente

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ('nome', 
				  'sobrenome',
				  'email', 
				  'senha',
				  'email', 
				  'senha', 
				  'telefone', 
				  'sexo',
				  'tipo_endereco',
				  'cep',
				  'rua',
				  'numero',
				  'bairro', 
				  'info_referencia', 
				  'cidade', 
				  'estado')