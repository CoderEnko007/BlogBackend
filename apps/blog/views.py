from django.shortcuts import render
from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from datetime import datetime

from blog.models import Category, Tag, Post
from blog.serializers import CategorySerializer, TagSerializer, PostSerializer
from blog.filters import PostFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = page_size
    page_query_param = 'p'
    max_page_size = 1000


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('create_time')
    serializer_class = PostSerializer
    pagination_class = PostPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = PostFilter
    search_fields = ('title', 'summary', 'category__name', 'tags__name', 'author__username')
    ordering_fields = ('create_time', 'modify_time', 'click_nums')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_nums += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        post = serializer.save()
        post.modify_time = datetime.now()
        post.save()

