from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    
    path('groups/new/', group_create_view, name='group_create'),
    path('groups/', group_list_view, name='group_list'),

    path('labels/new/', label_create_view, name='label_create'),
    path('labels/', label_list_view, name='label_list'),

    path('expenses/new/', expense_create_view, name='expense_create'),
    path('expenses/', expense_list_view, name='expense_list'),
    
    path("income/new/", income_create_view, name="income_create"),
    path("income/", income_list_view, name="income_list"),
    path('income/edit/<int:pk>/', income_edit_view, name='income_edit'),
    path('income/delete/<int:pk>/', income_delete_view, name='income_delete'),
]
