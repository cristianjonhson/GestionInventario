from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def agregar_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'agregar_producto.html', {'form': form})