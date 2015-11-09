from django.shortcuts import render
from suplemix.produtos.models import Produto
from suplemix.produtos.models import Categoria
from suplemix.carrocel.models import Carrocel
from suplemix.carrinho.models import Carrinho
from suplemix.carrinho.models import ItemCarrinho


# Create your views here.
def home(request):
	#request.session.set_expiry(120000)
	request.session.clear_expired()
	debug = ''

	if 'carrinho_id' not in request.session.keys():
		Carrinho.objects.all().delete()
		ItemCarrinho.objects.all().delete()
	else:
		try:
			the_id = request.session['carrinho_id']
			carrinho = Carrinho.objects.get(id=the_id)
			debug = 'Acessou o carrinho'

			itens = carrinho.itemcarrinho_set.all()
			request.session['itens_total'] = itens.count()
		except:
			the_id = None
			if Carrinho.objects.all().count() > 0:
				Carrinho.objects.all().delete()
				debug = 'Foi deletados todos carrinhos'

				carrinho = None
				request.session['itens_total'] = 0
			else:
				debug = 'carrinhos vazios'
			
	categorias = Categoria.objects.all()
	produtos   = Produto.objects.all()
	carrocel   = Carrocel.objects.all()
	return render(request, 'core/index.html', {'produtos': produtos, 'categorias': categorias, 'carrocel': carrocel, 'debug': debug})
	#return render(request, 'core/index.html')
