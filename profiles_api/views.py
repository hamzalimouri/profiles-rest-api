from django.db.models.query import QuerySet
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


class UserProfileViewSets(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
