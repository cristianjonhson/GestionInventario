# views.py

from django.shortcuts import render
from .models import Producto
from django.shortcuts import get_object_or_404


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle.html', {'producto': producto})

def actualizar_inventario(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        producto.cantidad = cantidad
        producto.save()
    return render(request, 'productos/actualizar.html', {'producto': producto})
