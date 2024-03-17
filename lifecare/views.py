from django.contrib.auth.models import User
from . import serializers
from rest_framework import viewsets


class UsersViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    