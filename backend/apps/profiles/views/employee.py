from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.profiles.models import EmployeeProfile
from apps.profiles.forms import EmployeeUpdateForm, EmployeeCreateForm

class EmployeeListView(LoginRequiredMixin, ListView):
    model = EmployeeProfile
    context_object_name = "employees"
    template_name = "profiles/employee/list.html"
    paginate_by  = 20

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = EmployeeProfile
    context_object_name = "employee"
    template_name = "profiles/employee/detail.html"

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = EmployeeProfile
    form_class = EmployeeCreateForm
    template_name = "profiles/employee/create.html"
    success_url = reverse_lazy("profiles:employee_list")

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = EmployeeProfile
    form_class = EmployeeUpdateForm
    template_name = "profiles/employee/update.html"
    success_url = reverse_lazy("profiles:employee_list")

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = EmployeeProfile
    template_name = "profiles/employee/delete.html"
    success_url = reverse_lazy("profiles:employee_list")

