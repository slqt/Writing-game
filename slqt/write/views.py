#coding=utf8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from write.models import Write
def index(request):
    s=Write.objects.get(name="WeizhongTu")
    return render(request, 'user/index.html',{'name':s})

def hello(request):
    return HttpResponse("Hello world")

def add(request):
    a =  request.GET.get('a', 0)
    b =  request.GET.get('b', 0)
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )