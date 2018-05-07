from django.contrib import admin
from .models import *

# Register your models here.
class BookInfoInAdmin(admin.TabularInline):
    #后台关联
    model = Heroinfo
    extra = 4

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']#列表分列
    list_filter = ['btitle']#过滤器
    search_fields = ['btitle']#搜索
    list_per_page = 10 #分页
    inlines = [BookInfoInAdmin]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','hgender','hcontent','hbook']
    list_filter = ['hgender','hbook']


admin.site.register(Bookinfo,BookInfoAdmin)
admin.site.register(Heroinfo,HeroInfoAdmin)
