from django import forms
from .models import Cliente, Reparacion

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
        }

class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = [
            'equipo',
            'tecnico',
            'fecha_ingreso',
            'fecha_entrega',
            'problema_reportado',
            'diagnostico',
            'solucion',
            'costo',
            'estado'
        ]
        widgets = {
            'equipo': forms.Select(attrs={'class': 'form-select'}),
            'tecnico': forms.Select(attrs={'class': 'form-select'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_entrega': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'problema_reportado': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describa el problema reportado'}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Diagnóstico inicial (opcional)'}),
            'solucion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Solución aplicada (opcional)'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }