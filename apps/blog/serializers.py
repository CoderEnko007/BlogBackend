# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from blog.models import Category, Tag, Post
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20, label='分类')
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    def validate(self, attrs):
        record_name = Category.objects.filter(name=attrs['name'])
        if record_name:
            raise serializers.ValidationError({'name': '该分类已存在'})
        return attrs

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['nums']


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=15, label='标签')
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    def validate(self, attrs):
        record_name = Tag.objects.filter(name=attrs['name'])
        if record_name:
            raise serializers.ValidationError({'name': '该标签已存在'})
        return attrs

    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ['nums']


class ListPostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = serializers.StringRelatedField(label='分类')
    tags = serializers.StringRelatedField(many=True, label='标签')
    create_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    modify_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'summary', 'content', 'category', 'tags', 'create_time', 'modify_time', 'click_nums')
        read_only_fields = ['click_nums']


class DefaultPostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    title = serializers.CharField(required=True, min_length=6,
                                  validators=[UniqueValidator(queryset=Post.objects.all(), message="改标题已存在")],
                                  error_messages={
                                      'min_length': '标题不能小于6个字符',
                                      'required': '请填写标题',
                                      'blank': '请填写标题',
                                  })
    category = serializers.PrimaryKeyRelatedField(label='分类', queryset=Category.objects.all())
    content = serializers.CharField(required=True, label='正文',
                                    error_messages={
                                        'required': '文章正文不能为空',
                                        'blank': '文章正文不能为空'
                                    })
    tags = serializers.PrimaryKeyRelatedField(many=True, label='标签', queryset=Tag.objects.all())
    create_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    modify_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

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
