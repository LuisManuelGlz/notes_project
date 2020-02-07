from django import forms
from .models import Note

# formulario para crear y editar notas
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note # definimos el modelo con el que trabajará el formulario
        fields = ['title', 'description'] # los campos title y description serán los únicos que se mostrarán en el formulario
        
        # personalizamos los campos con clases de Bootstrap
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Title',
                    'autofocus': True
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols': False,
                    'rows': False,
                    'placeholder': 'Description'
                }
            ),
        }