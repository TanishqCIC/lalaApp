from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

print('hi2')
urlpatterns = [
    url('add', views.add, name="Index"),
    url('articles', views.ArticleList.as_view()),
    url('shops', views.ShopList.as_view()),
    url('users', views.User.as_view()),
    url(r'^$', views.index, name="Index")
]

urlpatterns = format_suffix_patterns(urlpatterns)