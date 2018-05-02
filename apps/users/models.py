from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(default='', max_length=100, verbose_name='昵称')
    email = models.EmailField(default='', verbose_name='邮箱')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    gender = models.CharField(max_length=8, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
    desc = models.TextField(default='', verbose_name='描述')
    logo = models.ImageField(max_length=200, upload_to='logo/', verbose_name='头像标志')

    class Meta:
        verbose_name = '用戶信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username