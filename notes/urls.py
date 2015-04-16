from django.conf.urls import include, url
from django.contrib import admin

from .views import note_createview, note_listview, note_detailview

urlpatterns = [
	url(r'^notes/new/$', note_createview.as_view(), name='note_new'),
	url(r'^notes/$', note_listview.as_view(), name='notes'),
	url(r'^notes/(?P<pk>[\w\-\W]+)/$', note_detailview.as_view(), name='note_detail'),

]

