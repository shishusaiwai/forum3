from django.conf.urls import url

from .views import article_list


urlpatterns = [
    url(r'^list/', article_list),
]
