from django.conf.urls import include, url
from suplemix.clientes.views import novo_cliente, editar_cliente, login_cliente, autentica_login

urlpatterns = [
	url(r'^novo-cliente/$', novo_cliente, name='novo_cliente'),
	url(r'^editar-cliente/(?P<id>\d+)$', editar_cliente, name='editar_cliente'),
	url(r'^login-cliente/$', login_cliente, name='login_cliente'),
	url(r'^autentica-login/$', autentica_login, name='autentica_login'),
]