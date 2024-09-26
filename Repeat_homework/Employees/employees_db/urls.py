from django.urls import path
from django.views.generic import ListView, DetailView
from .views import EmployeeCreateView, EmployeeListView, EmployeeUpdateView, EmployeeDeleteView, Employee

urlpatterns = [
    path("",
         EmployeeListView.as_view(),
         name="employees_list"),
    path("<int:pk>/",
         DetailView.as_view(template_name="employee_detail.html",
                                         model=Employee),
         name="employee_detail"),
    path("create/", EmployeeCreateView.as_view(), name="employee_create"),
    path("update/<int:pk>/", EmployeeUpdateView.as_view(), name="employee_update"),
    path("delete/<int:pk>/", EmployeeDeleteView.as_view(), name="employee_delete"),
]