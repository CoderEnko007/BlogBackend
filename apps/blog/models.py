from django.db import models
from users.models import UserProfile

from DjangoUeditor.models import UEditorField
from datetime import datetime


# Create your models here.
class Category(models.Model):
    """
    博客类别
    """
    name = models.CharField(max_length=100, verbose_name='类别名')
    nums = models.IntegerField(default=0, null=True, blank=True, verbose_name='总数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField(max_length=100, verbose_name='标签名')
    nums = models.IntegerField(default=0, null=True, blank=True, verbose_name='总数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章信息
    """
    title = models.CharField(max_length=100, verbose_name='标题')
    content = UEditorField(imagePath="blogs/images", width=1000, height=300, toolbars="besttome",
                              filePath="blogs/files/", default='', verbose_name='内容')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    modify_time = models.DateTimeField(default=datetime.now, verbose_name='最后一次修改时间')
    summary = models.TextField(verbose_name='文章摘要', null=True, blank=True)
    click_nums = models.IntegerField(default=0, verbose_name='浏览次数')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章类别')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='文章标签')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='文章作者')

    class Meta:
        verbose_name = '文章信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title