from django.conf.urls import include, url
from django.contrib import admin

from .views import Note_CreateView, Note_ListView, Note_DetailView

urlpatterns = [
	url(r'^new/$', Note_CreateView.as_view(), name='note_new'),
	url(r'^$', Note_ListView.as_view(), name='notes'),
	url(r'^(?P<pk>[\w\-\W]+)/$', Note_DetailView.as_view(), name='note_detail'),

]
