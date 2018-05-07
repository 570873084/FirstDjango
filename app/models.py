from django.db import models

# Create your models here.
#书名和图书发布时间，与英雄为一对多关系
class Bookinfo(models.Model):

    btitle = models.CharField(max_length=20)
    bpub_date =models.DateTimeField()
    def __str__(self):
        return self.btitle

#英雄名，性别，英雄简介，所属图书
class Heroinfo(models.Model):
    name = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000,blank=True)
    #外键链接
    hbook = models.ForeignKey(Bookinfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
