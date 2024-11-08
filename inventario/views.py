from django.shortcuts import render

from .models import Categoria, Producto
from django.db.models import Q 
from django.db.models import Count, Sum, Avg 



# Create your views here.

def listado_categorias_view(request):
    contexto = {}
    categorias = Categoria.objects.all()
    contexto['categorias'] = categorias
    
    return render(request, 'categorias.html', contexto)

def listado_productos_view(request):
    contexto = {}
    productos = []
    
    nombre = request.GET.get('nombre')
    precio_min = request.GET.get('precio_min')
    
    contexto['nombre'] = nombre
    contexto['precio_min'] = precio_min

    productos = Producto.objects.all()
    
    resultado = Producto.objects.aggregate(total=Count('id'))
    
    contexto['cantidad_productos'] = resultado["total"]


    
    if nombre:
        productos = productos.filter(Q(nombre__icontains=nombre) | Q(descripcion__icontains=nombre))
        
    if precio_min:
        productos = productos.filter(precio__gte=precio_min)
        
    contexto['productos'] = productos
    
    
    return render(request, 'productos.html', contexto)