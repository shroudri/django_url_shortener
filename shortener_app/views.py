from django.http import HttpResponse
from django.shortcuts import render, redirect
from shortener_app.models import Url
import datetime
import random

from shortener_app.forms import UrlForm

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def create(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
                full_url = request.POST.get('full_url')
                shortened_uri = random.randint(1000, 9999)

                # Create a new patient entry in the database using the Patient model
                url = Url(full_url=full_url, shortened_uri=shortened_uri)
                url.save()

                return HttpResponse(f"Data successfully inserted!\r\nYour shortened URL is: http://127.0.0.1:8000/{shortened_uri}")
    else:
        form = UrlForm()
    return render(request, 'create.html', {'form': form})

def redirect(request, uri):
    url = Url.objects.get(shortened_uri=uri)
    destination = url.full_url
    return HttpResponse(destination)