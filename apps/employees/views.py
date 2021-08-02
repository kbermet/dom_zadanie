from django.shortcuts import render

# Create your views here.

from .models import Employee
from django.views.generic import View, DetailView

# Create your views here.

class EmployeesPageView(View):

    def get(self, request):
        employees = Employee.objects.filter(is_active=True)
        return render(request, 'employees_page.html', context={'employees': employees})


class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employee_detail.html'