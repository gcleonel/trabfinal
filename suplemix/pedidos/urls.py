from django.conf.urls import include, url
from suplemix.pedidos.views import enviar_email, gerar_pedido, meus_pedidos

urlpatterns = [
    url(r'^enviar-email/$', enviar_email, name='enviar_email'),
    url(r'^gerar-pedido/$', gerar_pedido, name='gerar_pedido'),
    url(r'^meus-pedidos/$', meus_pedidos, name='meus_pedidos'),
]