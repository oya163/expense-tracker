"""URL module for Income app"""

from django.urls import path

from . import views

urlpatterns = [
    path("incometypes/", views.IncomeTypeList.as_view()),
    path("incomes/<slug:user_id>", views.IncomeList.as_view()),
    path("incomesdetail/<slug:user_id>", views.IncomeDetail.as_view()),
]
