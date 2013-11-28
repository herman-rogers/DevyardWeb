from   django.shortcuts import render_to_response
from   django.http import HttpResponse
from   django.http import StreamingHttpResponse
###Things for the Blog
from   django.core.paginator import Paginator, InvalidPage, EmptyPage
from   django.core.urlresolvers import reverse
from   models import *
import datetime

def homepage( request ):
    now = datetime.datetime.now( )
    return render_to_response('DevyardHomepage.html', {'current_date': now} )
def dreamhearth( request ):
    now = datetime.datetime.now( )
    return render_to_response( "DreamHearth.html", {"current_date": now } )
def blogmain( request ):
    ###Here are the main posts
    posts = Post.objects.all( ).order_by( "-created" );
    paginator = Paginator( posts, 3 )
    
    try: page = int( request.GET.get( "page", "1" ) )
    except ValueError: page = 1
    
    try:
        posts = paginator.page( page )
    except ( InvalidPage, EmptyPage ):
        posts = paginator.page( paginator.num_pages )
        
    return render_to_response( "PopulateBlog.html", dict( posts=posts, user=request.user ) )