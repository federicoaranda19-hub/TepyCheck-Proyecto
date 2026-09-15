from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Tecnico, Equipo, Reparacion
from .forms import ClienteForm, ReparacionForm
from django.contrib.auth.decorators import login_required

# Lo dejamos sin @login_required para que la portada sea pública
def index(request):
    context = {"mensaje": "Ofrecemos servicios de reparación de computadoras, mantenimiento y soporte técnico."}
    return render(request, "myapp/index.html", context)

# ----------------- CLIENTES -----------------

@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'myapp/clientes.html', {'clientes': clientes})

@login_required
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:clientes')
    else:
        form = ClienteForm()
    return render(request, 'myapp/agregar_cliente.html', {'form': form})

@login_required
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

@login_required
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('myapp:clientes')
    return render(request, 'myapp/eliminar_cliente.html', {'cliente': cliente})

# ----------------- TECNICOS Y EQUIPOS -----------------

@login_required
def tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'myapp/tecnicos.html', {'tecnicos': tecnicos})

@login_required
def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'myapp/equipos.html', {'equipos': equipos})

# ----------------- REPARACIONES -----------------

@login_required
def reparaciones(request):
    reparaciones = Reparacion.objects.all()
    return render(request, 'myapp/reparacion.html', {'reparaciones': reparaciones})

@login_required
def agregar_reparacion(request):
    if request.method == 'POST':
        form = ReparacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:reparaciones')
    else:
        form = ReparacionForm()
    return render(request, 'myapp/agregar_reparacion.html', {'form': form})

@login_required
def editar_reparacion(request, pk):
    reparacion = get_object_or_404(Reparacion, pk=pk)
    if request.method == 'POST':
        form = ReparacionForm(request.POST, instance=reparacion)
        if form.is_valid():
            form.save()
            return redirect('myapp:reparaciones')
    else:
        form = ReparacionForm(instance=reparacion)
    return render(request, 'myapp/editar_reparacion.html', {'form': form, 'reparacion': reparacion})

@login_required
def eliminar_reparacion(request, pk):
    reparacion = get_object_or_404(Reparacion, pk=pk)
    if request.method == 'POST':
        reparacion.delete()
        return redirect('myapp:reparaciones')
    return render(request, 'myapp/eliminar_reparacion.html', {'reparacion': reparacion})