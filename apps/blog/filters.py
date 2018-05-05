# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters

from blog.models import Post, Category, Tag
from users.models import UserProfile


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(name='title', lookup_expr='icontains', label='文章标题')
    content = filters.CharFilter(name='content', lookup_expr='icontains', label='文章内容')
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())
    tags = filters.ModelChoiceFilter(queryset=Tag.objects.all())
    author = filters.ModelChoiceFilter(queryset=UserProfile.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags', 'author']
