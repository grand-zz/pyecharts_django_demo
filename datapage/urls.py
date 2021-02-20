# coding=utf-8
from django.conf.urls import url
from . import views
app_name = 'datapage'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.index),
    url(r'^chart/$', views.chart),
    url(r'^test/$', views.test, name='test')
]