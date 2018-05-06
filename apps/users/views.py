from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins

from .models import UserProfile
from .serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
