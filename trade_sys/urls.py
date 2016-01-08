"""order_ack_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import view

urlpatterns = [
	url(r'^admin/',include(admin.site.urls),name='admin_index'),
    url(r'^Trade_Works/',include('Trade_Works.urls'), name='Trade_Works_urls'),
    url(r'^Trade_Models/',include('Trade_Models.urls'),name='Trade_Model_urls'),
    url(r'^',include('Trade_Works.urls'),name='Trade_sys_index'),
    url(r'^$',include('Trade_Works.urls'),name='default_index')
]
