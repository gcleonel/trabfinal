"""suplemix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from suplemix.core import urls as core_urls
from suplemix.produtos import urls as produtos_urls
from suplemix.carrinho import urls as carrinho_urls
from suplemix.clientes import urls as clientes_urls
from suplemix.pedidos import urls as pedidos_urls
from django.conf import settings


urlpatterns = [
    url(r'', include(core_urls, namespace='core')),
    url(r'^produtos/', include(produtos_urls, namespace='produtos')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^carrinho/', include(carrinho_urls, namespace='carrinho')),
    url(r'^clientes/', include(clientes_urls, namespace='clientes')),
    url(r'^pedidos/', include(pedidos_urls, namespace='pedidos')),
    # url(r'^pedidos/(?P<slug>[\w-]+)/$', '', name='adicionar_carrinho'),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]

