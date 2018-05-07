from django.shortcuts import render
#from django.template import RequestContext,loader
from app.models import *
# Create your views here.

from django.http import HttpResponse
import datetime

def firstPage(request):
    sss = 'My First Page'
    now_time = datetime.datetime.now()
    html = '<html><head>aa</head><body><h1>%s </h1><p>%s</p></body></html>'%(sss,now_time)
    return HttpResponse(html)

def index(request):
    #temp =loader.get_template('app/index.html')

    #return HttpResponse(temp.render())
    boooList = Bookinfo.objects.all()
    heroList = Heroinfo.objects.all()
    context={'title':'你好！','list':boooList,'hero':heroList}
    return  render(request,'app/index.html',context)