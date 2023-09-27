from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin


class UserCustomViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
