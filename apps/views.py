from django.shortcuts import render
from django.http import HttpResponse
from apps.models import *
from django.db.models import Max


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
    # list = BookInfo.books.filter(heroinfo__hcontent__contains='六')筛选英雄名包含六的书名
    # list = BookInfo.books2.filter(pk__lte=3)筛选id小于等于3的
    # Max1 = BookInfo.books.aggregate(Max(pk)) id最大的
    # list = BookInfo.books.filter(pk__lt=F('bcommet'))id小于评论数的
    # list = BookInfo.books.filter(pk__lt =3,btitle__contains='1')and用法
    # list = BookInfo.books.filter(Q(pk__lt =3)|Q(btitle__contains='1'))or用法
    book = BookInfo.objects.get(pk=id)
    heroli = book.heroinfo_set.all()
    context = {'hero':heroli}
    return render(request,'hero.html',context)
