from django.contrib.auth.models import User, Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Group.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
