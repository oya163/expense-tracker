"""
Serializer module for IncomeType, Income
"""

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Income, IncomeType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "id")


class IncomeTypeSerializer(serializers.ModelSerializer):
    """IncomeTypeSerializer"""

    class Meta:
        model = IncomeType
        fields = "__all__"


class IncomeSerializer(serializers.ModelSerializer):
    """IncomeSerializer"""

    class Meta:
        model = Income
        fields = "__all__"
