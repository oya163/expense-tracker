"""
Serializer module for ExpenseType, Expense
"""

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Expense, ExpenseType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "id")


class ExpenseTypeSerializer(serializers.ModelSerializer):
    """ExpenseTypeSerializer"""

    class Meta:
        model = ExpenseType
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    """ExpenseSerializer"""

    class Meta:
        model = Expense
        fields = "__all__"
