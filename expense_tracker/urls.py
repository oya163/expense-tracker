"""URL module for Expense app"""

from django.urls import path

from . import views

urlpatterns = [
    path("expensetypes/", views.ExpenseTypeList.as_view()),
    path("expenses/<slug:user_id>", views.ExpenseList.as_view()),
]
