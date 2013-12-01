from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from models import Post

urlpatterns = patterns('',
    url(r'^$', "DevyardWeb.views.blogmain"),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
                            model=Post,
                            template_name="userpost.html")),
    url(r'^archives/$', ListView.as_view(
                            queryset=Post.objects.all().order_by("-created"),
                            template_name="archives.html")),
    url(r'^tag/(?P<tag>[\w|\W]+)$', 'DevyardWeb.views.Tags',),
)
