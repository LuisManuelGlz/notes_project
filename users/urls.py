from django.urls import path
from django.contrib.auth import views as auth_views # llamamos a las CBV genéricas
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    # llamamos al login y le pasamos el template login.html, ya que por defecto utiliza otro template
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]