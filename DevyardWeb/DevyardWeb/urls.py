from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'DevyardWeb.views.homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^dreamhearth/", "DevyardWeb.views.dreamhearth"),
    url(r"^blog/", "DevyardWeb.views.blogmain")
)
