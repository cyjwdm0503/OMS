__author__ = 'root'

from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^show/$',views.show,{"id":'123','pwd':'321'},name='test_show'),
    url(r'^detail/(?P<ooid>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<currentpage>[0-9]+)/$', views.index, name='Trade_Work_index'),
    url(r'^search/(?P<ooid>[0-9]+)/$',views.search,name='search'),
    url(r'^search/$',views.search,{'ooid':'0'},name='search_index'),
    url(r'^$',views.index,{'currentpage':'1'},name="Trade_Works_default_index"),
]
