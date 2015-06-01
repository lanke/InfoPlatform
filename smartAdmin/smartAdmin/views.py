#coding=utf-8
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render



def home(request):
   
    return render_to_response('index.html',locals(),RequestContext(request))



def dashboard(request):
   
    return render_to_response('dashboard.html',locals(),RequestContext(request))