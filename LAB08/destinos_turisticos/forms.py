from django import forms
from .models import DestinosTuristicos


class DestinoForm(forms.ModelForm):
    class Meta:
        model = DestinosTuristicos
        fields = ['nombreCiudad', 'descripcionCiudad', 'imagenCiudad', 'precioTour', 'ofertaTour']
        labels = {
            'nombreCiudad': 'Nombre de la Ciudad',
            'descripcionCiudad': 'Descripción',
            'imagenCiudad': 'Imagen',
            'precioTour': 'Precio del Tour (S/.)',
            'ofertaTour': '¿En oferta?',
        }
        widgets = {
            'nombreCiudad': forms.TextInput(attrs={'placeholder': 'Ej: Cusco'}),
            'descripcionCiudad': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe el destino...'}),
            'precioTour': forms.NumberInput(attrs={'placeholder': '0.00'}),
        }
