"""djangoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from apps import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first',views.first),
    path('jquery-1.12.4.js',views.jquery),
    re_path('^(<id>\d+)$',views.hero),#<关键字名>关键字参数用法，没有则使用位置参数匹配
    path('apps/',include('apps.urls',namespace='apps'))#namespace在include中，name在path中，用于反向解析

]
