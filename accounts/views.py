from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView

class LoginView(FormView):
	form_class = AuthenticationForm
	template_name = 'accounts/login.html'
	success_url = '/contactos/'

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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
    else:
        form = UserCreationForm()
    return render(
        request, 'accounts/register.html', {'form': form}
    )