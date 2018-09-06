from django.db import models

# Create your model

class BookInfoMange(models.Manager):
    def get_queryset(self):
        return super(BookInfoMange,self).get_queryset().filter()  #重写get_queryset方法
    def create(cls,title,autor,pub_date):  #第二种方法,在管理器中使用对象方法，推荐使用这种方法
        b = BookInfo()
        b.btitle =title
        b.autor = autor
        b.bpub_date = pub_date   #b = BookInfo.books2.create(参数) b.save()
        return b

class BookInfo(models.Model):
    #init方法会报错，因为继承的类Model里已经在用init,重写会直接覆盖Model中的init，导致里面的init不能用
    # ，可以调用类方法@classmethod
    btitle = models.CharField(max_length=20)
    autor = models.CharField(max_length=20,verbose_name='作者') #verbose_name 为admin页面显示名字
    bpub_date = models.DateTimeField(db_column='发布时间')#db_column为数据库列名
    books = models.Manager()#自定义模型类 和默认object一样 BookInfo.books.all() ==BookInfo.object.all()查询
    books2 = BookInfoMange()
    def __str__(self):
        return self.btitle
    class Meta:
        db_table ='bookinfo'#修改数据库表的名称，默认为应用名_模型名 apps_bookinfo
    @classmethod
    def create(cls,title,autor,pub_date):  #调用类方法的参数，不能用self，self调用init方法里的参数
        b = BookInfo()
        b.btitle =title
        b.autor = autor
        b.bpub_date = pub_date   #b = BookInfo.create(参数) b.save()
        return b

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE,db_column='book1')
