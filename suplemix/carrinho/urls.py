from django.conf.urls import include, url
from suplemix.carrinho.views import add_carrinho, view, remover_item_carrinho, editar_item_carrinho, autenticacao, login, endereco_entrega,log_out

urlpatterns = [
	url(r'^view$', view, name='view'),
    url(r'^adicionar-carrinho/([0-9]+)/$', add_carrinho, name='add_carrinho'),
    url(r'^editar-item-carrinho/$', editar_item_carrinho, name='editar_item_carrinho'),
    url(r'^remover-item-carrinho/([0-9]+)/$', remover_item_carrinho, name='remover_item_carrinho'),
    url(r'^autenticacao/$', autenticacao, name='autenticacao'),
    url(r'^login/$', login, name='login'),
    url(r'^endereco-entrega/$', endereco_entrega, name='endereco_entrega'),
    url(r'^logout/$', log_out, name='log_out'),
]
