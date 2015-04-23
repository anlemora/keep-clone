from django import forms

from .models import Note

class note_creation_form(forms.ModelForm):

	title = forms.CharField(label="Title")
	content = forms.CharField(label="", widget=forms.Textarea)

	class Meta:
		model = Note
		exclude = ('user',)