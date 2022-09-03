from django.shortcuts import render,  redirect
from Apps.forms import *
from Apps.models import *
import random

def Inicio (request):

    return render(request, 'index.html')


def Registro_Cliente(request):
    if request.method == 'POST':
        Formulario = Formulario_cliente(request.POST)

        if Formulario.is_valid():
            data = Formulario.cleaned_data

            lineaTelefonica1 = Linea_telefonica(Numero_celular = data.get('Numero_celular'),Ex_compañia = data.get('Ex_compañia'))
            lineaTelefonica1.save()

            cliente1 = Cliente(Nombre_cliente = data.get('Nombre_cliente'), Email_cliente = data.get('Email_cliente'), Dni_cliente = data.get('Dni_cliente'))
            cliente1.save()

            empleados = {
                'Messi': 43123453,
                'Cr7': 34328765,
                'Cristina': 673264,
                'Coscu': 7963274,
                'Momo': 34723233,
                'Ibai': 57519324

            }
            empleado, dni = random.choice(list(empleados.items()))

            Empleado1 = Empleado(Nombre_empleado = empleado, Dni_empleado = dni)
            Empleado1.save()

            return redirect ('AppsClienteFormulario')
        
                
    Lineas = Linea_telefonica.objects.all()
    Clientes = Cliente.objects.all()
    Empleados = Empleado.objects.all()

    context = {
        'form': Formulario_cliente(),
        'lineas': Lineas,
        'clientes': Clientes,
        'empleados': Empleados,
    }
    return render(request, 'Apps/clienteFormulario.html', context)
