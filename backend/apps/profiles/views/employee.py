from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.core.mixins import SearchableListViewMixin
from django.contrib.auth.models import Group
from django.db import transaction
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from apps.profiles.models import EmployeeProfile
from apps.profiles.forms import EmployeeUpdateForm, EmployeeCreateForm
from apps.accounts.constants import EMPLOYEE_GROUP

User = get_user_model()

class EmployeeListView(LoginRequiredMixin, PermissionRequiredMixin,SearchableListViewMixin, ListView):
    permission_required = "profiles.view_employeeprofile"
    model = EmployeeProfile
    context_object_name = "employees"
    template_name = "profiles/employee/list.html"
    paginate_by  = 20
    raise_exception = True

    search_fields = [
        "employee_number",
        "user__username",
        "user__first_name",
        "user__last_name",
    ]

class EmployeeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "profiles.view_employeeprofile"
    model = EmployeeProfile
    context_object_name = "employee"
    template_name = "profiles/employee/detail.html"
    raise_exception = True

class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = "profiles.add_employeeprofile"
    form_class = EmployeeCreateForm
    template_name = "profiles/employee/create.html"
    success_url = reverse_lazy("profiles:employee_list")
    raise_exception = True

    @transaction.atomic
    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data["username"],
            email=form.cleaned_data["email"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            password=form.cleaned_data["password"],
        )

        group = Group.objects.get(
            name=EMPLOYEE_GROUP
        )
        user.groups.add(group)
        EmployeeProfile.objects.create(
            user=user,
            employee_number=form.cleaned_data["employee_number"],
            hire_date=form.cleaned_data["hire_date"],
        )

        messages.success(
            self.request,
            "Successfully created employee profile!"
        )

        return super().form_valid(form)

class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "profiles.change_employeeprofile"
    model = EmployeeProfile
    form_class = EmployeeUpdateForm
    template_name = "profiles/employee/update.html"
    success_url = reverse_lazy("profiles:employee_list")
    raise_exception = True

    def form_valid(self, form):
        messages.success(
            self.request,
            "Successfully updated employee profile!"
        )
        return super().form_valid(form)

class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "profiles.delete_employeeprofile"
    model = EmployeeProfile
    template_name = "profiles/employee/delete.html"
    success_url = reverse_lazy("profiles:employee_list")
    raise_exception = True

    def form_valid(self, form):
        user = self.object.user
        messages.success(
            self.request,
            "Successfully deleted employee profile!")
        response = super().form_valid(form)
        user.delete()
        return response

