from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import UserProfile
from .serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_object(self):
        """
        GET {HOST}/user/{id} id随意填写，用户获取当前登录用户的信息
        :return:
        """
        return self.request.user

    def get_permissions(self):
        # if (self.action == "update"):
        #     return [permissions.IsAuthenticated()]
        # else:
            return [permissions.IsAuthenticated()]
