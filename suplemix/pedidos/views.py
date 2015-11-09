from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail
from suplemix.clientes.models import Cliente
from suplemix.carrinho.models import Carrinho
from suplemix.pedidos.models import Pedido, ItemPedido

# Create your views here.

def enviar_email(request, id):
	pedido = Pedido.objects.get(id=id)
	if 'cliente_email' not in request.session.keys():
		return redirect(reverse("carrinho:autenticacao"))
	else:
		cliente = Cliente.objects.get(email=request.session['cliente_email'])
		from_email = settings.EMAIL_HOST_USER

		title_msg = 'Olá, '+cliente.nome
		html_msg = """
			<h1>Olá, """+cliente.nome+"""</h1><br>
			Recebemos seu pedido<br>
			Você será informado(a), por e-mail, sobre o andamento do pedido até a chegada ao endereço escolhido.
			<br>
			Nº do pedido: """+str(pedido.id)+"""
			"""
		send_mail('Recebemos seupedido', title_msg, from_email, ['leonelads7@gmail.com'], html_message = html_msg,fail_silently=True)
		return redirect(reverse('core:home'))

def gerar_pedido(request):
	if 'cliente_email' not in request.session.keys():
		return redirect(reverse('carrinho:autenticacao'))
	else:
		if 'carrinho_id' in request.session:
			cliente        = Cliente.objects.get(email=request.session['cliente_email'])
			carrinho       = Carrinho.objects.get(id=request.session['carrinho_id'])
			pedido         = Pedido()
			pedido.cliente = cliente
			
			#if cliente:
			#	return redirect(reverse('carrinho:view'))
			
			valor_total = 0
			itens = carrinho.itemcarrinho_set.all()

			for i in itens:
				valor_total += i.total

			pedido.qnt_itens = itens.count()
			pedido.total     = valor_total
			pedido.email_cliente     = cliente.email
			pedido.cep       = cliente.cep
			pedido.rua       = cliente.rua
			pedido.bairro    = cliente.bairro
			pedido.numero    = cliente.numero
			pedido.cidade    = cliente.cidade
			pedido.uf        = cliente.estado
			pedido.status    = 'P'
			pedido.save()

			
			for item in itens:
				item_pedido          = ItemPedido()
				item_pedido.qnt      = item.quantidade
				item_pedido.pedido   = pedido
				item_pedido.subtotal = item.total
				item_pedido.produto  = item.produto
				item_pedido.save()

			msg = 'Obrigado por comprar na suplemix!'
			limpar_sessao(request)
			enviar_email(request, pedido.id)
		else:
			return redirect(reverse('carrinho:view'))

	return render(request, 'pedidos/sucesso_pedidos.html', {'msg':msg, 'pedido': pedido})


def limpar_sessao(request):
	try:
		if 'carrinho_id' in request.session:
			del request.session['carrinho_id']
			request.session['itens_total'] = 0
	except:
		pass

def meus_pedidos(request):
	meus_pedidos = None
	try:
		if 'cliente_email' in request.session:
			cliente  = Cliente.objects.get(email=request.session['cliente_email'])
			meus_pedidos = Pedido.objects.filter(cliente=cliente)
		else:
			return redirect(reverse('clientes:login_cliente'))
	except:
		pass

	return render(request, 'pedidos/meus-pedidos.html', {'meus_pedidos': meus_pedidos})