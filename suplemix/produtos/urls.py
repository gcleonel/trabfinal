from django.conf.urls import url
from suplemix.produtos.views import lista_produtos
from suplemix.produtos.views import detalhe_produto

urlpatterns = [
    url(r'^lista-produtos/$', lista_produtos, name='lista_produtos'),
    url(r'^detalhe-produto/(?P<id>\d+)$', detalhe_produto, name='detalhe_produto'),
    url(r'^$', lista_produtos, name=''),
]
