from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import StreamingHttpResponse
import datetime
def homepage(request):
    now = datetime.datetime.now()
    return render_to_response('DevyardHomepage.html', {'current_date': now})