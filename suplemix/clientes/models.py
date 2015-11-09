from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Cliente(models.Model):
	nome             = models.CharField(u'Nome', max_length=100)
	sobrenome        = models.CharField(u'Sobrenome',max_length=100)
	email            = models.CharField(u'E-mail',max_length=50, unique=True)
	senha            = models.CharField(u'Senha',max_length=50, default=None)
	telefone         = models.CharField(u'Telefone', max_length=14)
	celular       	 = models.CharField(u'Celular', max_length=14)
	data_cadastro    = models.DateField(("Data Cadastro"), auto_now_add=True)
	data_atualizacao = models.DateField(("Data Atualização"), auto_now_add=True)
	OFERTA_CHOICES   = (('N', 'NÃO'), ('S', 'SIM'))
	recebe_oferta    = models.CharField(u'Recebe ofertas',max_length=1, choices=OFERTA_CHOICES)

	SEXO_CHOICES     = (('M', 'Masculino'), ('F', 'Feminino'))
	sexo             = models.CharField(u'Sexo',max_length=1, choices=SEXO_CHOICES)
	cep           = models.CharField(u'Cep',max_length=50)
	cidade           = models.CharField(u'Cidade',max_length=50)
	rua              = models.CharField(u'Rua',max_length=100)
	bairro           = models.CharField(u'Bairro',max_length=100)
	info_referencia  = models.CharField(u'Informaçoes de referência',max_length=100)
	numero = models.CharField(max_length=100)
	TIPO_ENDERECO_CHOICES = (('0', 'Apartamento'), ('1', 'Casa'), ('2', 'Comercial'), ('3', 'Outros'))
	tipo_endereco = models.CharField(max_length=1, choices=TIPO_ENDERECO_CHOICES)

	ESTADO_CHOICES = (
	    ('AC', 'Acre'), 
	    ('AL', 'Alagoas'),
	    ('AP', 'Amapá'),
	    ('BA', 'Bahia'),
	    ('CE', 'Ceará'),
	    ('DF', 'Distrito Federal'),
	    ('ES', 'Espírito Santo'),
	    ('GO', 'Goiás'),
	    ('MA', 'Maranão'),
	    ('MG', 'Minas Gerais'),
	    ('MS', 'Mato Grosso do Sul'),
	    ('MT', 'Mato Grosso'),
	    ('PA', 'Pará'),
	    ('PB', 'Paraíba'),
	    ('PE', 'Pernanbuco'),
	    ('PI', 'Piauí'),
	    ('PR', 'Paraná'),
	    ('RJ', 'Rio de Janeiro'),
	    ('RN', 'Rio Grande do Norte'),
	    ('RO', 'Rondônia'),
	    ('RR', 'Roraima'),
	    ('RS', 'Rio Grande do Sul'),
	    ('SC', 'Santa Catarina'),
	    ('SE', 'Sergipe'),
	    ('SP', 'São Paulo'),
	    ('TO', 'Tocantins')
	)
	estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)


	def __str__(self):
		return self.email