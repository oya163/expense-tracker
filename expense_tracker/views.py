"""View module for Expense"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404
from django.db.models import Subquery

from .models import Expense, ExpenseType
from .serializers import (
    ExpenseTypeSerializer,
    ExpenseSerializerRead,
    ExpenseSerializerWrite,
)


class ExpenseTypeList(APIView):
    def get(self, request, format=None):
        expense_type = ExpenseType.objects.all()
        serializer = ExpenseTypeSerializer(expense_type, many=True)
        return Response(serializer.data)


class ExpenseList(APIView):
    def get(self, request, user_id, format=None):
        expenses = Expense.objects.all().filter(user_id=user_id)
        serializer = ExpenseSerializerRead(expenses, many=True)
        return Response(serializer.data)
