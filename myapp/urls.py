from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('tecnicos/', views.tecnicos, name='tecnicos'),
    path('equipos/', views.equipos, name='equipos'),
    path('reparaciones/', views.reparaciones, name='reparaciones'),
]