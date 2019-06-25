from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': True}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
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

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 4:
            raise forms.ValidationError('Password must be at least 4 characters')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password do not match')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email is already in use')
        return email

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class AuthenticationFormWithStyle(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': True}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']