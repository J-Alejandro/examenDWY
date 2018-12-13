from django import forms
from .models import Producto , Tienda

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = (
            'nombreTienda',
            'nombreSucursal',
            'direccion',
            'ciudad',
            'region',
        )
        labels={
            'nombreTienda':'Nombre Tienda',
            'nombreSucursal':'Nombre Sucursal',
            'direccion':'Direccion',
            'ciudad':'Ciudad',
            'region':'Region',
        }
        widgets={
            'nombreTienda':forms.TextInput(attrs={'class':'form-control'}),
            'nombreSucursal':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'region':forms.TextInput(attrs={'class':'form-control'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = (
            'nombreProducto',
            'costoPresupuestado',
            'costoReal',
            'tienda',
            'notaAdicional',
        )

        labels = {
            'nombreProducto':'Nombre Producto',
            'costoPresupuestado':'Costo Presupuestado',
            'costoReal':'Costo Real',
            'tienda':'Tienda',
            'notaAdicional':'Nota Adicional',
        }

        widgets = {
            'nombreProducto':forms.TextInput(attrs={'class':'form-control'}),
            'costoPresupuestado':forms.TextInput(attrs={'class':'form-control'}),
            'costoReal':forms.TextInput(attrs={'class':'form-control'}),
            'tienda':forms.Select(attrs={'class':'form-control'}),
            'notaAdicional':forms.TextInput(attrs={'class':'form-control'}),
            
        }