# FirstDjango
Django web
django

一.pycharm专业版可以一键部署django环境

mvt框架
m -models  负责与数据库交互   需要定义模型类：指定属性及类型，已确定表的结构   迁移   通过后台管理admin：创建管理员，启动服务器，注册admin.py

v -views   视图：接受请求，逻辑处理，调用数据，输出响应（templates）    需要配置url

t -templates 模板  

二.无专业版

1 创建项目

django-admin startproject 项目名

2 创建app
python manage.py startapp app名

# settings配置
# 将自己的app添加到这里
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]
# 在这里我们修改mysql数据库               #需要注意mysql编码问题
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'DjRecord',    #你的数据库名称,需要mysql里有这个数据库

        'USER': 'root',   #你的数据库用户名

        'PASSWORD': '', #你的数据库密码

        'HOST': '', #你的数据库主机，留空默认为localhost

        'PORT': '3306', #你的数据库端口

    }

}
#设置字体和时区
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'


#设置app文件下的models.py模型类
例如
	from django.db import models

	# Create your models here.
	#书名和图书发布时间，与英雄为一对多关系
	class Bookinfo(models.Model):

    		btitle = models.CharField(max_length=20)
    		bpub_date =models.DateTimeField()

	#英雄名，性别，英雄简介，所属图书
	class Heroinfo(models.Model):
    		name = models.CharField(max_length=10)
    		hgender = models.BooleanField()
    		hcontent = models.CharField(max_length=1000)
    		#外键链接
    		hbook = models.ForeignKey(Bookinfo,on_delete=models.CASCADE)



# 我们用的是pymysql，所以需要在项目名这个目录下的__init__.py文件添加：
import pymysql
pymysql.install_as_MySQLdb()

# 配置templates路径
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 配置static路径
STATIC_URL = '/static/'
STATICFILES_DIRS=(
    # 告诉django static的路径
    os.path.join(BASE_DIR,"static"),

)

# 运行项目
python manage.py runserver  127.0.0.1:8080

# 同步数据库,假如修改model.py，增加方法def的话，不需要迁移
#生成迁移
python manage.py makemigrations
#执行迁移
python manage.py migrate


#输入到数据库
python manage.py shell            

from app.models import *

b =Bookinfo()
b.btitle ='abc'
b.save()

#创建超级管理员账户，后台管理，增删改查数据 localhost/admin

python manage.py createsuperuser 

#向admin后台管理中注册模型，打开admin.py

from django.contrib import admin
from models import Bookinfo

class BookInfoInAdmin(admin.TabularInline):#或者admin.StackedInline
	#后台关联
    	model = Heroinfo
   	extra = 3 

class BookInfoAdmin(admin.ModelAdmin):
	list_display = ['id','btitle','bpub_date']#列表分列
    	list_filter = ['btitle']#过滤器
    	search_fields = ['btitle']#搜索
    	list_per_page = 1 #分页
    	inlines = [BookInfoInAdmin]#内关联
admin.site.register(Bookinfo，BookInfoAdmin)


#视图编辑views.py 
from django.shortcuts import render
from django.template import RequestContext,loader        ***********
from django.http import HttpResponse                     ***********
def index(request): 
    	#加载文件
    	temp =loader.get_template('app/index.html')     #index.html在templates文件中

    	return HttpResponse(temp.render())#渲染


#编辑urls.py

from django.contrib import admin
from django.urls import path
from app import views           ********

urlpatterns = [
    	path('admin/', admin.site.urls),
    	path('firstpage',views.firstPage),
    	path('index',views.index)
                            ]
