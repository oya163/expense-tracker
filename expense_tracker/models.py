"""
Models module for Expense Tracker
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class ExpenseType(models.Model):
    """Model class for ExpenseType"""

    name = models.CharField(max_length=255)

    class Meta:
        """Meta class"""

        managed = True
        db_table = "expense_type"

    def __str__(self):
        return str(self.name)


class Expense(models.Model):
    """Model class for Expense"""

    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
    )
    amount = models.FloatField(default=0.00)
    expensetype = models.ForeignKey(
        ExpenseType, on_delete=models.CASCADE, default=1
    )
    remarks = models.TextField(blank=True, null=True, default="")
    expense_date = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class"""

        managed = True
        db_table = "expense"

    def __str__(self):
        return str(self.name)
