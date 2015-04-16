from django.shortcuts import render

from django.views.generic import CreateView, ListView, DetailView

from .models import Note

from .forms import note_creation_form

class note_createview(CreateView):
	model = Note
	form_class  = note_creation_form
	success_url = '/notes/'
	template_name = 'create_note.html'

class note_listview(ListView):
	model = Note
	template_name = 'notes.html'

class note_detailview(DetailView):
	model = Note
	template_name = 'note_detail.html'
