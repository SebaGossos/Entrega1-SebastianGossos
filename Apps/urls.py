from django.urls import path

from Apps.views import *

urlpatterns = [
path ('',Inicio, name='AppInicio'),
path('FormularioCliente/', Registro_Cliente, name='AppsClienteFormulario'),

]