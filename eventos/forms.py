from django import forms
from .models import Evento, Usuario, RegistroEvento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin',
                  'lugar', 'capacidad_maxima', 'categoria', 'organizador']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'telefono']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model = RegistroEvento
        fields = ['usuario', 'evento', 'estado']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
