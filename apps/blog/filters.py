# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters

from blog.models import Post


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(name='title', lookup_expr='icontains', label='文章标题')
    content = filters.CharFilter(name='content', lookup_expr='icontains', label='文章内容')

    class Meta:
        model = Post
        fields = ['title', 'content']
