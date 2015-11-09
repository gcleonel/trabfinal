from django.db import models

# Create your models here.

class Carrocel(models.Model):
	imagem = models.ImageField(upload_to="carrocel-principal/images/")
	status = models.CharField(max_length=1)
	nome_img = models.CharField(max_length=100)

	def __str__(self):
		return self.nome_img