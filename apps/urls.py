from django.contrib import admin
from django.urls import path,re_path
from apps import views

app_name = '[apps]'  #include需要添加app_name
urlpatterns = [
    re_path('^$',views.index,name='index')

]
