from django.shortcuts import render

from django.views.generic import FormView, ListView, DetailView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import note_creation_form
from .models import Note


class Note_ListView(ListView):
	model = Note
	template_name = 'notes/notes.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		
		return super(Note_ListView, self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(Note_ListView, self).get_context_data(**kwargs)

		context.update({'notes': self.get_notes()})

		return context

	def get_notes(self):
		user = self.request.user
		notes = Note.objects.filter(user=user)
		return notes


class Note_CreateView(FormView):

	model = Note
	form_class  = note_creation_form
	success_url = '/notes/'
	template_name = 'notes/create_note.html'

	def form_valid(self, form):
		user = self.request.user
		form = form.save(commit = False)
		form.user = user
		form.save()

		return super(Note_CreateView, self).form_valid(form)



class Note_DetailView(DetailView):
	model = Note
	template_name = 'notes/note_detail.html'
