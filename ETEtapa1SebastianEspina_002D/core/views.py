from django.shortcuts import render,redirect, get_object_or_404
from .models import usuario ,Producto
from .forms import UsuarioForm, ProductoForm
# Create your views here.
def index(request):
    return render(request,'index.html')

  
def tienda(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'tienda.html', data)  


def login_registro(request):
    if request.method=='POST': 
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()    #save() reemplaza al insert
            return redirect('index')
    else: 
        usuario_form=UsuarioForm()
    return render(request, 'core/login_registro.html', 
    {'usuario_form':usuario_form})


def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data['form'] = formulario

    
    return render(request, 'core/agregar.html', data)


def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'core/listar.html', data)    



def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario 


    return render(request, 'core/modificar.html', data)  


def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    producto.delete()
    return redirect(to="listar_productos")     






 


