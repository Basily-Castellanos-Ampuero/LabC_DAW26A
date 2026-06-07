from django import forms
from .models import Autor, Libro, Genero


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email', 'pais']


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'generos', 'año', 'descripcion']
        widgets = {
            'generos': forms.CheckboxSelectMultiple(),
        }


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']


class EmailForm(forms.Form):
    destinatario = forms.EmailField(label='Correo del destinatario')
    asunto = forms.CharField(max_length=200, label='Asunto')
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')
