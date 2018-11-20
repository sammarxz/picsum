from django.conf.urls import url
from .views import placeholder, index

#urls
urlpatterns = (
    url(r'^(?P<width>[0-9]+)x(?P<height>[0-9]+)/(?P<color>[a-fA-F0-9]{6})$', 
        placeholder, name='placeholder'),
    url(r'^$', index, name='homepage'),
)
