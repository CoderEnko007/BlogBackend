# -*- coding: utf-8 -*-
from rest_framework import serializers

from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'nick_name', 'email', 'birthday', 'gender', 'desc', 'logo')
