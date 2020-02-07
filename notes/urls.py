from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.NotesView.as_view(), name='all-notes'),
    path('add/', views.AddNoteView.as_view(), name='add-note'),
    path('edit/<int:pk>/', views.EditNoteView.as_view(), name='edit-note'),
    path('delete/<int:pk>/', views.DeleteNoteView.as_view(), name='delete-note'),
]