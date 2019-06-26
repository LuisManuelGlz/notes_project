from django.urls import path
from .views import (
    NotesView,
    AddNoteView,
    EditNoteView,
    DeleteNoteView
)

urlpatterns = [
    path('', NotesView.as_view(), name='all-notes'),
    path('add/', AddNoteView.as_view(), name='add-note'),
    path('edit/<int:pk>/', EditNoteView.as_view(), name='edit-note'),
    path('delete/<int:pk>/', DeleteNoteView.as_view(), name='delete-note'),
]