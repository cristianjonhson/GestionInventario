from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from gestion.views import lista_productos, detalle_producto

urlpatterns = [
    path('list/', lista_productos, name='listar_productos'),
    path('listview/', detalle_producto, name='detalle_producto') 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


"""
urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/<int:pk>/', views.detalle_categoria, name='detalle_categoria'),
    path('categoria/nueva/', views.nueva_categoria, name='nueva_categoria'),
    path('categoria/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categoria/<int:pk>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),
] """
