# -*- coding: utf-8 -*-
import xadmin
from .models import Category, Tag, Post


class CategoryAdmin(object):
    list_display = ["name", 'nums']
    list_editable = ['name']


class TagAdmin(object):
    list_display = ['name', 'nums']
    list_editable = ['name']


class PostAdmin(object):
    list_display = ['title', 'author', 'summary', 'click_nums', 'category', 'tags']
    style_fields = {"content": "ueditor"}

    # def get_context(self):
    #     context = super(PostAdmin, self).get_context()
    #     if 'form' in context:
    #         test = context['form'].fields['author']
    #         print('aaa')
        # return context


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Post, PostAdmin)