from django.urls import path
from .views import home , agregarProducto,listarProducto,eliminarProducto



urlpatterns = [
    path('',home, name="home"),
    path('agregarProducto/',agregarProducto,name="agregarProducto"),
    path('listarProducto/',listarProducto,name="listarProducto"),
    path('eliminarProducto/<id>',eliminarProducto,name="eliminarProducto"),
]