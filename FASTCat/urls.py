from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic.base import RedirectView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import fastfurniture.forms
import fastfurniture.views

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', fastfurniture.views.gallery, name='gallery'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    url(r'^(?P<slug>[-\w]+)$', fastfurniture.views.AlbumDetail.as_view(), name='album'), #app.views.AlbumView.as_view()
     
    # Auth related urls
    
    url(r'^accounts/login/$', views.LoginView, name='login'),
    url(r'^logout$', views.LogoutView, { 'next_page': '/', }, name='logout'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
    path('gallery/', include('gallery.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'fastfurniture.views.handler404'




