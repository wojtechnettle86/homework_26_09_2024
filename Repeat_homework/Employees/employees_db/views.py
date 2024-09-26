from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.mixins import LoginRequiredMixin


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees_list.html'
    context_object_name = 'page_obj'
    paginate_by = 10


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employees_list')


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employees_list')


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employees_list')