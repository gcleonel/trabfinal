from django.shortcuts import render
from suplemix.produtos.models import Produto
from suplemix.produtos.models import Imagem

# Create your views here.

def lista_produtos(request):
	produtos = Produto.objects.all()
	return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def detalhe_produto(request, id):
	imgs    = Imagem.objects.filter(produto=id)
	produto = Produto.objects.get(id=id)
	return render(request, 'produtos/detalhe-produto.html', {'produto':produto, 'imgs':imgs})