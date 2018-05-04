# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from .models import UserProfile


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = 'XXX的博客'
    site_footer = '撸起袖子加油干'


# class UserProfile(object):
#     list_displey = ['username', 'nick_name', 'email', 'gender', 'desc']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)