from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from suplemix.clientes.forms import ClienteForm
from suplemix.clientes.models import Cliente

# Create your views here.

def novo_cliente(request):
	if request.method == 'POST':
		form_cliente = ClienteForm(request.POST)
		if form_cliente.is_valid():
			email = form_cliente.cleaned_data['email']
			form_cliente.save()
			request.session['cliente_email'] = email
			return redirect(reverse('carrinho:view'))
		else:
			print(form_cliente.errors)
	else:
		form_cliente = ClienteForm()
	return render(request, 'clientes/add_cliente.html', {'form_cliente': form_cliente})


def editar_cliente(request, id):
	cliente = Cliente.objects.get(id=id)
	if request.method == 'POST':
		form_cliente = ClienteForm(request.POST, instance=cliente)
		if form_cliente.is_valid():
			form_cliente.save()
			return redirect(reverse('carrinho:view'))
		else:
			print(form_cliente.errors)
	else:
		form_cliente = ClienteForm(instance=cliente)
	return render(request, 'clientes/editar_cliente.html', {'form_cliente': form_cliente})

def login_cliente(request):
	return render(request, "clientes/login.html")


def autentica_login(request):
	if request.method == 'POST':
		cliente = Cliente.objects.get(email=request.POST['email'])
		if not cliente:
			message = 'Registro não encontrado.'
			return render(request, "clientes/login.html", {'message': message})
		else:
			if cliente.senha == request.POST['senha']:
				request.session['cliente_email'] = request.POST['email']
				request.session['cliente_nome']  = cliente.nome
				return redirect(reverse("core:home"))
				#return render(request, "carrinho/view.html", {'cliente': cliente})
			else:
				message = 'Combinação de usuário e senha não encontrada.'
				return render(request, "clientes/login.html", {'message': message})

