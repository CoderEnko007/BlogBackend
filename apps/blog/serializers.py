# -*- coding: utf-8 -*-
from rest_framework import serializers

from blog.models import Category, Tag, Post
from users.serializers import UserSerializer
from users.models import UserProfile


class CategorySerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['nums']


class TagSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")

    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ['nums']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    category = serializers.PrimaryKeyRelatedField(required=True, label='分类', queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, label='标签', queryset=Tag.objects.all())
    # author = serializers.PrimaryKeyRelatedField(required=True, label='作者', queryset=UserProfile.objects.all())
    create_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")
    modify_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['click_nums']


class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'