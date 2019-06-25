from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

# Create your views here.
@login_required
def notes(request):
    print(request.user)
    context = {
        'notes': Note.objects.filter(user=request.user).order_by('-updated')
    }
    return render(request, 'notes/all_notes.html', context)

@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, f'Note added successfully')
            return redirect('all-notes')
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', { 'form': form })

@login_required
def edit_note(request, id):
    note = Note.objects.get(id=id)
    
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note.save()
            messages.success(request, f'Note edited successfully')
            return redirect('all-notes')
    else:
        form = NoteForm({'title': note.title, 'description': note.description})
    return render(request, 'notes/edit_note.html', { 'form': form })

@login_required
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    messages.success(request, f'Note deleted successfully')
    return redirect('all-notes')
