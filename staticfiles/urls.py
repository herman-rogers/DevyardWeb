from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, DetailView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from models import Post
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'DevyardWeb.views.homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^dreamhearth/", "DevyardWeb.views.dreamhearth"),
    url(r'^blog/', include('DevyardWeb.urlsblog')),
)
