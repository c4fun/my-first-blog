__author__ = 'laurichard'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # It means that Django will take everything that
    # you place here and transfer it to a view as a variable called pk
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]

