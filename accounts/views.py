from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import FormView

class LoginView(FormView):
	form_class = AuthenticationForm
	template_name = 'accounts/login.html'
	success_url = '/notes/'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(self.request, form.user_cache)
		
		return super(LoginView, self).form_valid(form)

	def dispatch(self, request, *args, **kwargs):
		#Validate that user is not already logged in.
		if request.user.is_authenticated():
			return redirect(self.success_url)
		else:
			return super(LoginView, self).dispatch(request, *args, **kwargs)


from django.contrib.auth.models import User
from .forms import RegistrationForm
# from django.contrib.auth.forms import UserCreationForm

class SignupView(FormView):
	model = User
	form_class = RegistrationForm
	template_name = 'accounts/signup.html'
	success_url = '/notes/'