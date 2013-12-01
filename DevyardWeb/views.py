from   django.shortcuts import render_to_response
from   django.http import HttpResponse, HttpResponseRedirect
###Things for the Blog
from   django.core.paginator import Paginator, InvalidPage, EmptyPage
from   django.core.urlresolvers import reverse
from   models import *

import datetime

def homepage( request ):
    posts = Post.objects.all( ).order_by( "-created" )[:50]
    paginator = Paginator( posts, 1000 ) 
    return render_to_response( "DevyardHomepage.html", dict( posts=posts, user=request.user ) )
def dreamhearth( request ):
    now = datetime.datetime.now( )
    return render_to_response( "DreamHearth.html", {"current_date": now } )
def Tags(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response( "Tags.html", {"posts":posts, "tag":tag})
###SAVED BUT UNUSED CODE -- FOR THE URLS
def blogmain( request ):
    ###Here are the main posts
    posts = Post.objects.all( ).order_by( "-created" )[:50]
    paginator = Paginator( posts, 1 )
    try: page = int( request.GET.get( "page", "1" ) )
    except ValueError: page = 1
    try:
        posts = paginator.page( page )
    except ( InvalidPage, EmptyPage ):
        posts = paginator.page( paginator.num_pages )
    return render_to_response( "PopulateBlog.html", dict( posts=posts, user=request.user ) )
