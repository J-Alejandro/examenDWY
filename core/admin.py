from django.contrib import admin
from .models import Producto, Tienda

# Register your models here.

class TiendaAdmin(admin.ModelAdmin):
    list_display=('nombreTienda','nombreSucursal','direccion','ciudad','region')
    search_fields=['nombreTienda','nombreSucursal']

class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombreProducto','costoPresupuestado','costoReal','tienda','notaAdicional')
    search_fields=['nombreProducto','tienda']
    

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Tienda, TiendaAdmin)