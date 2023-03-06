"""View module for Income"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenVerifySerializer

from django.http import Http404
from django.contrib.auth.models import User

from .models import Income, IncomeType
from .serializers import (
    IncomeTypeSerializer,
    IncomeSerializer,
)


class IncomeTypeList(APIView):
    def get(self, request, format=None):
        income_type = IncomeType.objects.all()
        serializer = IncomeTypeSerializer(income_type, many=True)
        return Response(serializer.data)


class IncomeList(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, user_id, format=None):
        # token = request.META.get("HTTP_AUTHORIZATION", " ").split(" ")[1]
        incomes = Income.objects.all().filter(user_id=user_id)
        serializer = IncomeSerializer(incomes, many=True)
        return Response(serializer.data)

    def post(self, request, user_id, format=None):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeDetail(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self, user_id, index):
        try:
            return Income.objects.get(id=index, user_id=user_id)
        except Income.DoesNotExist as exc:
            raise Http404 from exc

    def get(self, request, user_id, format=None):
        index = int(request.GET.get("id"))
        income = self.get_object(user_id, index)
        serializer = IncomeSerializer(income)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        index = int(request.GET.get("id"))
        income = self.get_object(user_id, index)
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        index = int(request.GET.get("id"))
        income = self.get_object(user_id, index)
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
