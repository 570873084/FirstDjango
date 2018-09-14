from django.shortcuts import render
from django.http import HttpResponse
from apps.models import *
from django.db.models import Max


# Create your views here.

def index(request):
    return HttpResponse('hello world')


def first(request):
    booklist = BookInfo.books.all()
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
    #a = request.GET['a'] 获取get参数，?a=1&b=2一键一值
    # a = request.GET['a'] ?a=1&a=2&a=3获取最后一个a值
    # a = request.GET.getlist('a') ?a=1&a=2&a=3获取所有a值
    book = BookInfo.books.get(pk=id)
    heroli = book.heroinfo_set.all()
    context = {'hero':heroli}
    return render(request,'hero.html',context)
#cookie练习
def cookieTest(request):
    response = HttpResponse() #构造response对象
    cookie = request.COOKIES
    if cookie.has_key('t1'):
        response.write(cookie['t1'])#往response中写入request的cookie
    #response.set_cookie('t1'为key,'abc'为value,过期时间)
    return response

#session练习
def session(request):
    uname = request.session[key值]
    # request.session.set_expiry(10)  10秒后过期
    # request.session.set_expiry(timedelta(days=5))
    # request.session.set_expiry(0) 浏览器关闭后过期
    # request.session.set_expiry(None)  永不过期
    context = {'uname':uname}
    return render(request,'',context)

#html转义练习
def htmlTest(request):
    context = {'t1':'<h1>123<h1>'}
    return render(request,'hero.html',context)


