# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.index),
    url(r'^chart/$', views.chart)
]