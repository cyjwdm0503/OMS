from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404

def index(request):
    index_buffer="this is Trade_Models.index"
    return  HttpResponse(index_buffer)

def show(request,id,pwd ):
    buffer ="this is models show %s" % id
    return HttpResponse(buffer)