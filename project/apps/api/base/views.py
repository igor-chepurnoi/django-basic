from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.versioning import NamespaceVersioning

from project.apps.api.base.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.

    retrieve:
    Return a user instance.

    list:
    Return all users, ordered by most recently joined.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    versioning_class = NamespaceVersioning


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.

    retrieve:
    Return a group instance.

    list:
    Return all groups.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    versioning_class = NamespaceVersioning
