# -*- coding: utf-8 -*-
from rest_framework import serializers

from blog.models import Category, Tag, Post
from users.serializers import UserSerializer


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
    category = CategorySerializer()
    tags = TagSerializer()
    author = UserSerializer()
    create_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")
    modify_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['click_nums']