__author__ = 'root'

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404


def index(request,name):
    index_string = "THIS IS ORDER_ACK_TEST %s"
    return  HttpResponse(index_string % name)