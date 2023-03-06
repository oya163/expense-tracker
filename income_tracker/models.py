"""
Models module for Income Tracker
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class IncomeType(models.Model):
    """Model class for IncomeType"""

    name = models.CharField(max_length=255)

    class Meta:
        """Meta class"""

        managed = True
        db_table = "income_type"

    def __str__(self):
        return str(self.name)


class Income(models.Model):
    """Model class for Income"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
    )
    amount = models.FloatField(default=0.00)
    income_type = models.ForeignKey(
        IncomeType, on_delete=models.CASCADE, default=1
    )
    remarks = models.TextField(blank=True, null=True, default="")
    income_date = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class"""

        managed = True
        db_table = "income"

    def __str__(self):
        return str(self.income_type)
