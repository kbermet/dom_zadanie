from django.urls import path

from .views import EmployeesPageView, EmployeeDetailView

urlpatterns = [
    path('', EmployeesPageView.as_view(), name='employees_list'),
    path('<int:pk>', EmployeeDetailView.as_view(), name='employees_detail_url'),
]