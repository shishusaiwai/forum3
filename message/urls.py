from django.conf.urls import url

from .views import message_list, read_message


urlpatterns = [
    url(r'^list/$', message_list, name="message_list"),
    url(r'^read/(?P<message_id>\d+)$', read_message, name="read_message"),
]
