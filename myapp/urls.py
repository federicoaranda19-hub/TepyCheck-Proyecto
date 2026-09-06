from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('tecnicos/', views.tecnicos, name='tecnicos'),
    path('equipos/', views.equipos, name='equipos'),
    path('reparaciones/', views.reparaciones, name='reparaciones'),

    # CRUD Clientes
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
]