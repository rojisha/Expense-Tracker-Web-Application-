from django.urls import path

from .views import ExpenseCreateView, ExpenseDeleteView, ExpenseListView, ExpenseUpdateView

urlpatterns = [
    path('', ExpenseListView.as_view(), name='expense_list'),
    path('create/', ExpenseCreateView.as_view(), name='expense_create'),
    path('<int:pk>/edit/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense_delete'),
]
