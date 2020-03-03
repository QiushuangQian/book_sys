from django.db import models

# Create your models here.
from django.utils import timezone

from user.models import MyUser


# 类别
class Category(models.Model):
    category_id = models.AutoField('序号', primary_key=True)
    category_name = models.CharField('类别名称', max_length=50)


# 书
class Book(models.Model):
    book_id = models.AutoField('序号', primary_key=True)
    name = models.CharField('书名', max_length=255)
    description = models.CharField('描述', max_length=255)
    author = models.CharField('作者', max_length=255)
    publisher = models.CharField('出版社', max_length=255)
    publish_date = models.CharField('出版时间', max_length=255)
    category = models.ForeignKey('类型（序号）', Category, on_delete=models.CASCADE)
    createDate = models.DateTimeField('记录创造时间', default=timezone.now)
    updateDate = models.DateTimeField('记录更新时间', default=timezone.now)
    product_id = models.IntegerField('商品编号', max_length=11)
    price = models.FloatField('价格', max_digits=9, decimal_places=2)
    views = models.IntegerField('浏览量', default=0)
    grade = models.FloatField('评分', max_digits=3, decimal_places=1, default=0)


# 书的图片
class BookImg(models.Model):
    img_id = models.AutoField('序号', primary_key=True)
    url = models.TextField('图片源')
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE,verbose_name='书籍')
    type = models.CharField('图片类型', max_length=20)


# 浏览记录
class BrowerHistory(models.Model):
    id = models.AutoField('序号', primary_key=True)
    createDate = models.DateTimeField('首次访问时间', default=timezone.now)
    updateDate = models.DateTimeField('访问更新时间', default=timezone.now)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE,verbose_name='用户')
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE,verbose_name='书籍')


# 购物车
class ShoppingCart(models.Model):
    id = models.AutoField('序号', primary_key=True)
    count = models.IntegerField('数量', max_length=11)
    createDate = models.DateTimeField('首次添加时间', default=timezone.now)
    updateDate = models.DateTimeField('再次添加时间', default=timezone.now)
    user_id = models.ManyToManyField(MyUser, on_delete=models.CASCADE,verbose_name='用户')
    book_id = models.ManyToManyField(Book, on_delete=models.CASCADE,verbose_name='书籍')


# 搜索记录
class SearchHistory(models.Model):
    id = models.AutoField('序号', primary_key=True)
    search = models.CharField('搜索内容', max_length=255)
    count = models.IntegerField('搜素次数', max_length=11)
    createDate = models.DateTimeField('首次搜索时间', default=timezone.now)
    updateDate = models.DateTimeField('再次搜索时间', default=timezone.now)
    user_id = models.ForeignKey( MyUser, on_delete=models.CASCADE,verbose_name='用户')


# 用户喜欢的书籍
class Favorite(models.Model):
    id = models.AutoField('序号', primary_key=True)
    createDate = models.DateTimeField('首次喜欢时间', default=timezone.now)
    updateDate = models.DateTimeField('再次喜欢时间', default=timezone.now)
    user_id = models.ManyToManyField(MyUser, on_delete=models.CASCADE,verbose_name='用户')
    book_id = models.ManyToManyField(Book, on_delete=models.CASCADE,verbose_name='书籍')
