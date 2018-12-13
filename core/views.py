from django.shortcuts import render,redirect
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
   
    
   
    if request.POST:
        form = ProductoForm(request.POST or None)
        if form.is_valid():

            prod = form.save(commit=False)
            #form.save()
            
            prod.save()

            grabo = True
            form = ProductoForm()
           
           
    else:
        form = ProductoForm()
    
    return render(request,'core/agregar_producto.html',{'form':form,'grabo':grabo})
    

def listarProducto(request):
    
    produ = Producto.objects.all()

    return render(request,'core/listar_producto.html',{
        'productos':produ})

def eliminarProducto(request,id):
    produ = Producto.objects.get(id=id)
    
    try:
        
        produ.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request,mensaje)

    return redirect('listarProducto')