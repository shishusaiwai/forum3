from django.conf.urls import url

from .views import upload_avatar


urlpatterns = [
    url(r'^uploadavatar/', upload_avatar),
]
