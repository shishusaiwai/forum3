from django.conf.urls import url

from .views import article_list


urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', article_list),
]
