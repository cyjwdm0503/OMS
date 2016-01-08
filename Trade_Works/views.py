from django.core.exceptions import  FieldError,FieldDoesNotExist
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import  render
from django.core.cache import cache
import  time
from django.views.decorators.cache import  cache_page

from  Trade_Models.models import  *

def FindOraderAck(index):
    order = OrderAck.objects.get(seqnum = index)
    return  order

@cache_page(10*1)
def index(request,currentpage):
    begin_time =  time.time()
    currentpage = int(currentpage,10)
    maxpage = (int)((Orders.objects.count()+9)/10)
    orders = cache.get(currentpage)
    if(orders == None):
        orders = Orders.objects.all().order_by('-ooid')[currentpage*10-10:currentpage*10]
        cache.set(currentpage,orders,10)
    maxpage = currentpage+2 if currentpage+2 <= maxpage else maxpage
    minpage = currentpage-2 if currentpage-2 > 1 else 1


    orders_dicts = {}
    for order in list(orders):
        order_dic = makedic(order.ooid)
        orders_dicts[str(order.ooid)] = order_dic


    content={'index_model_name':"Orders",
             'OrderAck_List':list(orders),
             'orders_dicts':orders_dicts,
             'minpage':minpage,
             'lastpage':currentpage-1,
             'currentpage':currentpage,
             'nextpage':currentpage+1,
             'maxpage':maxpage,
             'pages':range(minpage,maxpage+1)}

    xxx =   render(request,'index.html',content)
    end_time  = time.time()
    print 1000*(end_time-begin_time)
    return xxx

def show(request,id,pwd ):
    buffer ="this is models show %s" % id
    return HttpResponse(buffer)

def detail(request,ooid):
    dic = makedic(ooid)
    content={'dict':dic}

    return render(request,'detail.html',content)


def search(request,ooid):
    ooid = int(ooid,10)
    try:
    	  order = Orders.objects.get(ooid = ooid)
    except AttributeError:
        return HttpResponse("<p>Not Found</p>")
    except Orders.DoesNotExist:
	  return HttpResponse("<p>Not Found</p>")
    order_dic = makedic(ooid)
    content={'ooid':ooid,'order_dic':order_dic}

    search_index =  render(request,'search_index.html',content)
    return search_index


def makedic(ooid):
    ##dic = cache.get(ooid)
    if(None == None):
        create_order =  OrderCreate.objects.filter(ooid = ooid).order_by('tstamp')
        ack_order = OrderAck.objects.filter(ooid = ooid).order_by('tstamp')
        cancel_order = OrderCancel.objects.filter(ooid = ooid).order_by('tstamp')
        out_order = OrderOut.objects.filter(ooid = ooid).order_by('tstamp')
        accecpt_replace_order = OrderAcceptReplace.objects.filter(ooid = ooid).order_by('tstamp')
        reject_order = OrderReject.objects.filter(ooid = ooid).order_by('tstamp')
        reject_cancel_order = OrderRejectCancel.objects.filter(ooid = ooid).order_by('tstamp')
        replace_order = OrderReplace.objects.filter(ooid = ooid).order_by('tstamp')
        create_fills = FillCreate.objects.filter(ooid = ooid).order_by('tstamp')
        fills = Fills.objects.filter(ooid = ooid ).order_by('lstamp')
        order = Orders.objects.filter(ooid = ooid).order_by('lstamp')
        ordertransactionlog  = OrderTransactionLog.objects.filter(ooid = ooid).order_by('tstamp')
        close_order = OrderClose.objects.filter(ooid = ooid).order_by('tstamp')
        reject_replace_order = OrderRejectReplace.objects.filter(ooid = ooid).order_by('tstamp')

        dic = dict()
        dic = adddic(dic,create_order)
        dic = adddic(dic,list(ack_order))
        dic = adddic(dic,cancel_order)
        dic = adddic(dic,reject_cancel_order)
        dic = adddic(dic,out_order)
        dic = adddic(dic,replace_order)
        dic = adddic(dic,accecpt_replace_order)
        dic = adddic(dic,reject_order)
        dic = adddic(dic,create_fills)
        dic = adddic(dic,fills)
        dic = adddic(dic,order)
    #    dic = adddic(dic,ordertransactionlog)
        dic = adddic(dic,close_order)
        dic = adddic(dic,reject_replace_order)
        dic = sort(dic)
      ##  cache.set(ooid,dic,3)

    return dic

def adddic(dic,all_order):
    for order in all_order:
        try:
            dic[str(order.tstamp)]= order.getStr()
        except AttributeError:
            dic[str(order.lstamp)]= order.getStr()
    return dic

def sort(dic):
    items  = dic.items()
    items.sort()
    return items

