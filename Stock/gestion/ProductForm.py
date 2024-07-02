from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def home(request):
    return render(request, 'inventario/home.html')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/listar_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/crear_producto.html', {'form': form})
