# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = 'Backend App'

urlpatterns = [
    url(r'^', include('blue_backend.app.urls', namespace='app')),
    url(r'^api/', include('blue_backend.api.urls', namespace='api')),
    url(r'^admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)