import hashlib

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import etag

from .forms import ImageForm


# eTag
def generate_etag(request, width, height, color):
    content = 'Placeholder: {0}x{1}-{2}'.format(width, height, color)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()


#views
@etag(generate_etag)
def placeholder(request, width, height, color):
    form = ImageForm({'width': width, 'height': height, 'color': color})
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponseBadRequest('Invalid Image Request')

def index(request):
    return render(request, 'home.html', {})
