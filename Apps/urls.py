from django.urls import path

from Apps.views import *

urlpatterns = [
path ('',Inicio, name='AppInicio'),
path('formulario_cliente/', Registro_Cliente, name='AppsClienteFormulario'),
path('busqueda_cliente/',busqueda_cliente, name='AppsBusquedaCliente'),
path('resultado_busqueda_cliente/',resultado_busqueda_cliente, name='AppsResultadoBusquedaCliente')
]