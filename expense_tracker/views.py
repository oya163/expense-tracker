"""View module for Expense"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from .models import Expense, ExpenseType
from .serializers import (
    ExpenseTypeSerializer,
    ExpenseSerializer,
)


class ExpenseTypeList(APIView):
    def get(self, request, format=None):
        expense_type = ExpenseType.objects.all()
        serializer = ExpenseTypeSerializer(expense_type, many=True)
        return Response(serializer.data)


class ExpenseList(APIView):
    def get(self, request, user_id, format=None):
        expenses = Expense.objects.all().filter(user_id=user_id)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request, user_id, format=None):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetail(APIView):
    def get_object(self, user_id, index):
        try:
            return Expense.objects.get(id=index, user_id=user_id)
        except Expense.DoesNotExist as exc:
            raise Http404 from exc

    def get(self, request, user_id, format=None):
        index = int(request.GET.get("id"))
        expense = self.get_object(user_id, index)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        index = int(request.GET.get("id"))
        expense = self.get_object(user_id, index)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        index = int(request.GET.get("id"))
        expense = self.get_object(user_id, index)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
