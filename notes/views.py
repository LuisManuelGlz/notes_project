from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Note
from .forms import NoteForm
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
# @method_decorator(login_required, name='dispatch') # restringimos el acceso a menos que hayas inicias sesión
class NotesView(LoginRequiredMixin, ListView):
    # model = Note # definimos el modelo con el que trabajarán las vistas
    template_name = 'notes/all_notes.html' # definimos el template donde estarán todas las notas
    context_object_name = 'notes' # el contexto que usará el template
    # ordering = ['-updated']

    # redefinimos queryset para filtrar las notas por usuario
    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Note.objects.filter(user=user).order_by('-updated')

# @method_decorator(login_required, name='dispatch') # restringimos el acceso a menos que hayas inicias sesión
class AddNoteView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Note # definimos el modelo con el que trabajarán las vistas
    template_name = 'notes/add_note.html' # definimos el template para crear una nota
    form_class = NoteForm # usamos nuestro formulario ya creado
    success_url = reverse_lazy('notes:all-notes') # redireccionamos a todas las notas
    success_message = 'Note added siccessfully' # le decimos al usuario que la nota se creó exitosamente

    # redefinimos form_valid para decirle a la base de datos a quién pertenece la nota
    def form_valid(self, form):
        self.object = form.save(commit=False) # detenemos el guardado
        self.object.user = self.request.user # obtenemos al dueño de la nota por medio de la request y lo asignamos a la nota
        self.object.save() # guardamos la nota con el usuario ya establecido
        return super().form_valid(form)

# @method_decorator(login_required, name='dispatch') # restringimos el acceso a menos que hayas inicias sesión
class EditNoteView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Note # definimos el modelo con el que trabajarán las vistas
    template_name = 'notes/edit_note.html' # definimos el template para editar una nota
    form_class = NoteForm # usamos nuestro formulario ya creado
    success_url = reverse_lazy('notes:all-notes') # redireccionamos a todas las notas
    success_message = 'Note updated successfully' # le decimos al usuario que la nota se actualizó exitosamente

    """
        YA NO SE NECESITA ESTE form_valid PORQUE YA SE DEFINIÓ EL USUARIO EN AddNoteView
    """
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

# @method_decorator(login_required, name='dispatch') # restringimos el acceso a menos que hayas inicias sesión
class DeleteNoteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Note # definimos el modelo con el que trabajarán las vistas
    success_url = reverse_lazy('notes:all-notes') # redireccionamos a todas las notas
    success_message = 'Note deleted successfully' # le decimos al usuario que la nota se eliminó exitosamente

    # no tenía la intención de usar esta función pero no se mostraba el success_message
    # aún no sé con exactitud cómo funciona
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteNoteView, self).delete(request, *args, **kwargs)