from django.shortcuts import render
from django.contrib import messages
from .forms import TiendaForm, ProductoForm
from .models import Tienda, Producto
# Create your views here.

def home(request):
    return render(request,'core/index.html')

#Agregar producto, no me muestra las tiendas, debe haber un problema con "variables", ya que,
#Si esta primero que las llaves con form y grabo, muestra las tienes en el combobox
#Pero muere el combobox
def agregarProducto(request):
    grabo=False
    tiendas = Tienda.objects.all()

    variables ={
        'tiendas':tiendas
    }

    tiendas = variables
    variables = variables
    if request.POST:
        form = ProductoForm(request.POST or None)
        if form.is_valid():

            prod = form.save(commit=False)
            #form.save()
            prod.tienda = request.POST.get('cboTienda')
            prod.save()

            grabo = True
            form = ProductoForm()
            variables['mensaje'] = 'Guardado correctamente'
    else:
        form = ProductoForm()
    
    return render(request,'core/agregar_producto.html',{'form':form,'grabo':grabo},variables)
