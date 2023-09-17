"""
Serializers for the user API view
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
