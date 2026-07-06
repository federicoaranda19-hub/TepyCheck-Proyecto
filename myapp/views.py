from django.shortcuts import render
from .models import Cliente, Tecnico, Equipo, Reparacion

def index(request):
    context = {"mensaje": "Ofrecemos servicios de reparación de computadoras, mantenimiento y soporte técnico."}
    return render(request, "myapp/index.html", context)

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'myapp/clientes.html', {'clientes': clientes})

def tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'myapp/tecnicos.html', {'tecnicos': tecnicos})

def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'myapp/equipos.html', {'equipos': equipos})

def reparaciones(request):
    reparaciones = Reparacion.objects.all()
    return render(request, 'myapp/reparacion.html', {'reparaciones': reparaciones})