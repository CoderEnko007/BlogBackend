from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, mixins, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from datetime import datetime

from blog.models import Category, Tag, Post
from blog.serializers import CategorySerializer, TagSerializer, ListPostSerializer, DefaultPostSerializer, PostDetailSerializer
from blog.filters import PostFilter
from utils.permissions import IsOwnerOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if (self.action == "create")|(self.action == "update")|(self.action == "destroy"):
            return [permissions.IsAuthenticated()]
        else:
            return []


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_permissions(self):
        if (self.action == "create")|(self.action == "update")|(self.action == "destroy"):
            return [permissions.IsAuthenticated()]
        else:
            return []


class PostPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = page_size
    page_query_param = 'page'
    max_page_size = 1000


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-create_time')
    pagination_class = PostPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # permission_classes = (IsOwnerOrReadOnly, )

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = PostFilter
    search_fields = ('title', 'summary', 'category__name', 'tags__name', 'author__username')
    ordering_fields = ('create_time', 'modify_time', 'click_nums')

    @staticmethod
    def update_tags_num():
        tags = Tag.objects.all()
        for tag in tags:
            tag_post = Post.objects.filter(tags__name=tag.name)
            if tag_post:
                nums = tag_post.count()
                new_tag = Tag.objects.get(id=tag.id)
                new_tag.nums = nums
                new_tag.save()

    @staticmethod
    def update_category_num():
        categorys = Category.objects.all()
        for category in categorys:
            category_post = Post.objects.filter(category_id=category.id)
            if category_post:
                nums = category_post.count()
                new_category = Category.objects.get(id=category.id)
                new_category.nums = nums
                new_category.save()

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
        self.update_tags_num()
        self.update_category_num()

    def perform_create(self, serializer):
        post = serializer.save()
        self.update_tags_num()
        self.update_category_num()

    def perform_destroy(self, instance):
        instance.delete()
        self.update_tags_num()
        self.update_category_num()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        elif self.action == 'list':
            return ListPostSerializer
        else:
            return DefaultPostSerializer

    def get_permissions(self):
        if (self.action == "create")|(self.action == "update")|\
                (self.action == "destroy")|(self.action == 'partial_update'):
            permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
            return [permission() for permission in permission_classes]
        else:
            return []


class PostListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Post.objects.all().order_by('-create_time')
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

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        else:
            return ListPostSerializer


class AdminListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Post.objects.all().order_by('-create_time')
    serializer_class = ListPostSerializer
