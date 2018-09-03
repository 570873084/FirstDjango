from django.contrib import admin
from apps.models import *

# Register your models here.
class HeroInfoLine(admin.TabularInline):
    model = HeroInfo
    extra = 2

class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoLine]
    list_display = ['id','btitle','autor','bpub_date']
    list_filter = ['btitle']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname','hgender','hcontent','hbook']


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)


