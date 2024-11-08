from django.urls import path

from . import views

urlpatterns = [
    path('categorias/', views.listado_categorias_view, name="listado_categorias"),
    path('productos/', views.listado_productos_view, name="listado_productos"),
]
