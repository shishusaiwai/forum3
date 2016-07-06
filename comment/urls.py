from django.conf.urls import url

from .views import create_comment


urlpatterns = [
    url(r'^create/$', create_comment),
]
