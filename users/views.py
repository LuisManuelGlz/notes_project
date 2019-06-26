from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserCreationFormWithEmail
from django.contrib.auth.models import User
from django.views.generic import CreateView

# Create your views here.
class SignupView(SuccessMessageMixin, CreateView):
    template_name = 'users/signup.html' # definimos el template para crear un usuario
    form_class = UserCreationFormWithEmail # usamos nuestro formulario personalizado
    success_url = reverse_lazy('login') # redireccionamos al login
    success_message = 'You are registered' # le decimos al usuario que ya ha sido registrado