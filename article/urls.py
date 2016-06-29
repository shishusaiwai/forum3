from django.conf.urls import url

from .views import article_list, ArticleCreateView, ArticleDetailView


urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', article_list),
    url(r'^create/(?P<block_id>\d+)', ArticleCreateView.as_view()),
    url(r'^detail/(?P<pk>\d+)/$', ArticleDetailView.as_view()),
]
