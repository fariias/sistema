from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.home', name='home'),
    url(r'^clientes/', 'core.views.clientes', name='clientes'),
    url(r'^ccliente/', 'core.views.ccliente', name='ccliente'),
    url(r'^contratos/', 'core.views.contratos', name='contratos'),
    url(r'^ccontrato/', 'core.views.ccontrato', name='ccontrato'),
    url(r'^rastreadores/', 'core.views.rastreadores', name='rastreadores'),
    url(r'^crastreador/', 'core.views.crastreador', name='crastreador'),
]
