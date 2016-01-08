__author__ = 'root'

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^/show/',views.show,{"id":'123','pwd':'321'},name='model_show'),
    url(r'^$', views.index, name='order_ack_app_index'),
]