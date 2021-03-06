from django.urls import path
from .views import  index, tienda, login_registro, agregar_producto, listar_productos, modificar_producto, eliminar_producto


urlpatterns = [
    path ('', index, name="index"),

    path('tienda' , tienda, name='tienda'),
    path('login_registro', login_registro, name="login_registro"),
    path('agregar-producto', agregar_producto, name="agregar_producto"),
    path('listar-productos', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
]