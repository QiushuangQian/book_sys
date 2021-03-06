from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class MyUser(AbstractUser):
    nick_name = models.CharField('昵称', max_length=255)
    phone = models.CharField('手机号', max_length=11)
    address = models.CharField('地址', max_length=255)
    balance = models.FloatField('余额',max_digits=9, decimal_places=2)

    # 设置返回值
    def __str__(self):
        return self.username
