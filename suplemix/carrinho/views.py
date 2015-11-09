from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import decimal

# Create your views here.
from suplemix.carrinho.models import ItemCarrinho
from suplemix.carrinho.models import Carrinho
from suplemix.produtos.models import Produto
from suplemix.clientes.models import Cliente

def view(request):
	request.session.clear_expired()
	empty_msg = ''
	contexto = {}

	if not request.session.has_key('carrinho_id'):
		Carrinho.objects.all().delete()
		ItemCarrinho.objects.all().delete()
		empty_msg = 'Sua Cesta está vazia, por favor vá as compras.'
		contexto = {'empty':True, 'empty_msg': empty_msg}
	else:
		try:
			the_id = request.session['carrinho_id']
			carrinho = Carrinho.objects.get(id=the_id)
			debug = 'Acessou o carrinho'
			new_total = 0
			itens = carrinho.itemcarrinho_set.all()
			
			if itens.count() > 0:
				request.session['itens_total'] = itens.count()
				for item in itens:
					line_total = item.total
					new_total += line_total

				carrinho.total = new_total
				carrinho.save()
				contexto = {'carrinho': carrinho}
			else:
				empty_msg = "Sua Cesta está vazia, por favor vá as compras."
				contexto = {'empty':True, 'empty_msg': empty_msg}
				carrinho = None
				request.session['itens_total'] = 0
		except:
			the_id = None
			if Carrinho.objects.all().count() > 0:
				Carrinho.objects.all().delete()
				debug = 'Foi deletados todos carrinhos'
			else:
				debug = 'carrinhos vazios'
	
	return render(request, "carrinho/view.html", contexto)



	# 		
	# 	Carrinho.objects.all().delete()
	# 	empty_msg = "Seu Carrinho está vazio, por favor vá as compras."
	# 	contexto = {'empty':True, 'empty_msg': empty_msg}
	# 	carrinho = None
	# 	request.session['itens_total'] = 0	
	# else:
	# 	try:
	# 		the_id = request.session['carrinho_id']
	# 		carrinho = Carrinho.objects.get(id=the_id)
	# 		debug = 'Acessou o carrinho'
	# 	except:
	# 		the_id = None
	# 		if Carrinho.objects.all().count() > 0:
	# 			Carrinho.objects.all().delete()
	# 			debug = 'Foi deletados todos carrinhos'
	# 		else:
	# 			debug = 'carrinhos vazios'
		
	# 	if the_id:
	# 		new_total = 0
	# 		itens = carrinho.itemcarrinho_set.all()
	# 		if itens.count() > 0:
	# 			request.session['itens_total'] = itens.count()
	# 			for item in itens:
	# 				line_total = item.total
	# 				new_total += line_total

	# 			carrinho.total = new_total
	# 			carrinho.save()
	# 			contexto = {'carrinho': carrinho}
	# 		else:
	# 			empty_msg = "Seu Carrinho está vazio, por favor vá as compras."
	# 			contexto = {'empty':True, 'empty_msg': empty_msg}
	# 			carrinho = None
	# 			request.session['itens_total'] = 0
	#return render(request, "carrinho/view.html", contexto)
	


def add_carrinho(request, id):
	#request.session.set_expiry(120000)
	request.session.set_expiry(12000)

	try:
		the_id = request.session['carrinho_id']
	except:
		novo_carrinho = Carrinho()
		#session_id = request.session['session_key']
		novo_carrinho.save()
		request.session['carrinho_id'] = novo_carrinho.id
		the_id = request.session['carrinho_id']
		

	if the_id:
		carrinho = Carrinho.objects.get(id=the_id)

	itens = carrinho.itemcarrinho_set.all()
	produto = Produto.objects.get(id=id)

	produto_existe = False
	for it in itens:
		if produto.id == it.produto.id:
			produto_existe = True
			break
	
	if not produto_existe:
		novo_item = ItemCarrinho()
		novo_item.carrinho = carrinho
		novo_item.produto  = produto
		novo_item.total = produto.get_preco()
		novo_item.save()
	
	return redirect(reverse("carrinho:view"))
	

def remover_item_carrinho(request, id):
	try:
		the_id = request.session['carrinho_id']
		carrinho = Carrinho.objects.get(id=the_id)
	except:
		return redirect(reverse("carrinho:view"))

	item = ItemCarrinho.objects.get(id=id)
	#cartitem.delete()
	#item.carrinho = None
	item.delete()
	#send "success message"
	return redirect(reverse("carrinho:view"))

def editar_item_carrinho(request):
	if request.method == 'POST':
		idItem = request.POST.get('id')
		item = ItemCarrinho.objects.get(id=idItem)

		qtde = int(request.POST.get('qnt'))

		item.quantidade = qtde
		item.total = decimal.Decimal(qtde * item.produto.valor_venda)
		item.save()

	return redirect(reverse("carrinho:view"))


def autenticacao(request):
	email = ''
	try:
		email = request.session['cliente_email']
	except:
		pass

	if email: 
		return redirect(reverse("carrinho:endereco_entrega"))
	else:
		return render(request, "carrinho/autenticacao.html")
		

def login(request):
	if request.method == 'POST':
		cliente = Cliente.objects.get(email=request.POST['email'])
		if not cliente:
			message = 'Registro não encontrado.'
			return render(request, "carrinho/autenticacao.html", {'message': message})
		else:
			if cliente.senha == request.POST['senha']:
				request.session['cliente_email'] = request.POST['email']
				request.session['cliente_nome']  = cliente.nome
				return redirect(reverse("carrinho:view"))
				#return render(request, "carrinho/view.html", {'cliente': cliente})
			else:
				message = 'Combinação de usuário e senha não encontrada.'
				return render(request, "carrinho/autenticacao.html", {'message': message})


def endereco_entrega(request):
	cliente = Cliente.objects.get(email=request.session['cliente_email'])

	if cliente:
		msg = 'encontrou o cliente'
		return render(request, "carrinho/entrega.html", {'cliente': cliente, 'msg': msg})
	else:
		msg = 'não encontrou o cliente'
		return render(request, "carrinho/autenticacao.html", {'msg': msg})

def log_out(request):
	del request.session['cliente_email']
	del request.session['cliente_nome']
	return redirect(reverse("core:home"))
