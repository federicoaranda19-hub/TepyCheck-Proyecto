from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Tecnico, Equipo, Reparacion
from .forms import ClienteForm

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

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:clientes')
    else:
        form = ClienteForm()
    return render(request, 'myapp/agregar_cliente.html', {'form': form})


def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('myapp:clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'myapp/editar_cliente.html', {'form': form, 'cliente': cliente})


def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('myapp:clientes')
    return render(request, 'myapp/eliminar_cliente.html', {'cliente': cliente})