from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'autofocus': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': False, 'rows': False, 'placeholder': 'Description'}),
        }