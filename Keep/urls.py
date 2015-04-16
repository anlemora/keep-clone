from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('notes.urls')),
]


urlpatterns += staticfiles_urlpatterns() 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)