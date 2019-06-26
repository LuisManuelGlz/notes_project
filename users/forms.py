from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# formulario para crear un nuevo usaurio (pero con email)
class UserCreationFormWithEmail(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': True}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
    # email = forms.EmailField(required=True)

    class Meta:
        model = User # definimos el modelo con el que trabajará el formulario

        # los campos username, email, password1 y password2 (contraseña de confirmación) serán los únicos que se mostrarán en el formulario
        fields = ['username', 'email', 'password1', 'password2']

    """
            CON ESTO COMPROBAMOS QUE CADA CAMPO TIENE UN MÉTODO CLEAN_ALGO POR DEFECTO
            NOSOTROS LOS PODEMOS SOBREESCRIBIR
    """
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if username != 'marmota':
    #         raise forms.ValidationError('Marmota error')
    #     return username

    # redefinimos clean_password para que la contraseña sea mayor a 4 caracteres
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1') # recuperamos la contraseña
        if len(password1) < 4:
            raise forms.ValidationError('Password must be at least 4 characters') # mandamos un error para el usuario
        return password1

    # redefinimos clean_password2 (contraseña de confirmación) para que coincida con la primera contraseña
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1') # recuperamos la contraseña
        password2 = self.cleaned_data.get('password2') # recuperamos la contraseña de confirmación
        if password1 and password2 and password1 != password2: # si el usuario escribió dos contraseñas pero no coinciden
            raise forms.ValidationError('Password do not match') # mandamos un error para el usuario
        return password2

    # redefinimos clean_email para que el usuario no introduzca un email que ya exista
    def clean_email(self):
        email = self.cleaned_data.get('email') # recuperamos el email
        if User.objects.filter(email=email).exists(): # si el correo existe
            raise forms.ValidationError('The email is already in use') # mandamos un error a usuario
        return email

    # redefinimos save para encriptar la contraseña del usuario en la base de datos
    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user