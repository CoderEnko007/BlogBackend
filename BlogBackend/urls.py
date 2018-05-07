"""BlogBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

import xadmin
from BlogBackend.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from blog.views import CategoryViewSet, TagViewSet, PostViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'categorys', CategoryViewSet, base_name='categorys')
router.register(r'tags', TagViewSet, base_name='tags')
router.register(r'posts', PostViewSet, base_name='posts')
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ueditor/',include('DjangoUeditor.urls')),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    path('media/<path:path>/', serve, {'document_root': MEDIA_ROOT}),
    path('docs/', include_docs_urls(title='我的博客')),

    path('login/', obtain_jwt_token),

    url(r'^', include(router.urls)),
]
