from django.shortcuts import render
from .models import Note

def note_list_view(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

