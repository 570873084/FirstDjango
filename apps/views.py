from django.shortcuts import render
from django.http import HttpResponse
from apps.models import *


# Create your views here.

def index(request):
    return HttpResponse('hello world')


def first(request):
    booklist = BookInfo.objects.all()
    context = {'list':booklist}
    return render(request,'无缝滚动.html',context)

def jquery(request):
    return render(request,'jquery-1.12.4.js')

def hero(request,id):
    book = BookInfo.objects.get(pk=id)
    heroli = book.heroinfo_set.all()
    context = {'hero':heroli}
    return render(request,'hero.html',context)
