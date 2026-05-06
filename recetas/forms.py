from django import forms
from .models import Autor, Receta, Comentario


class AutorForm(forms.ModelForm):
    class Meta:
        model  = Autor
        fields = ['nombre', 'correo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs.update({'class': 'form-control'})


class RecetaForm(forms.ModelForm):
    class Meta:
        model  = Receta
        fields = ['titulo', 'ingredientes', 'preparacion', 'autor']
        widgets = {
            'ingredientes': forms.Textarea(attrs={'rows': 3}),
            'preparacion':  forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs.update({'class': 'form-control'})


class ComentarioForm(forms.ModelForm):
    class Meta:
        model  = Comentario
        fields = ['texto']
        widgets = {'texto': forms.Textarea(attrs={'rows': 2})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs.update({'class': 'form-control'})
