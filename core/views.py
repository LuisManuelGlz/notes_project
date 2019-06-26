from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'core/home.html' # definimos el template de la página principal

    # redefinimos get para pasarle el contexto title de forma personalizada
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Django and PostgreSQL'})

class AboutView(TemplateView):
    template_name = 'core/about.html' # definimos el template del about

    # redefinimos get para pasarle el contexto username de forma personalizada
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'username': request.user.username})
