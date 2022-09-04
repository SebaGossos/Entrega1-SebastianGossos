from django import forms

class Formulario_cliente (forms.Form):
    
    Ex_compañia = forms.CharField()
    Numero_celular = forms.IntegerField()
    Nombre_cliente = forms.CharField()
    Email_cliente = forms.EmailField()
    Dni_cliente = forms.IntegerField()

class BusquedaClienteFormulario(forms.Form):
    dni = forms.IntegerField()