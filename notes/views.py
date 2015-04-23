from django.shortcuts import render

from django.views.generic import FormView, ListView, DetailView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Note

from .forms import note_creation_form



class note_createview(FormView):

	model = Note
	form_class  = note_creation_form
	success_url = ''
	template_name = 'notes/create_note.html'

	def form_valid(self, form):
		user = self.request.user
		form = form.save(commit = False)
		form.user = user
		form.save()

		return super(note_createview, self).form_valid(form)


class note_listview(ListView):
	model = Note
	template_name = 'notes/notes.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		
		return super(note_listview, self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(note_listview, self).get_context_data(**kwargs)

		context.update({'notes': self.get_notes()})

		return context

	def get_notes(self):
		user = self.request.user
		notes = Note.objects.filter(user==user)
		return notes

class note_detailview(DetailView):
	model = Note
	template_name = 'notes/note_detail.html'
