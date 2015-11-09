from django.conf.urls import include, url
from suplemix.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]
