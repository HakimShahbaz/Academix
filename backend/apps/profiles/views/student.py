from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.core.mixins import SearchableListViewMixin
from django.contrib.auth.models import Group
from django.db import transaction
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, FormView
from django.urls import reverse_lazy

from apps.profiles.models import StudentProfile
from apps.profiles.forms import StudentCreateForm, StudentUpdateForm
from apps.accounts.constants import STUDENT_GROUP

User = get_user_model()

class StudentListView(LoginRequiredMixin, PermissionRequiredMixin,SearchableListViewMixin, ListView):
    permission_required = "profiles.view_studentprofile"
    model = StudentProfile
    template_name = "profiles/student/list.html"
    context_object_name = "students"
    paginate_by = 20
    raise_exception = True

    search_fields = [
        "student_number",
        "user__username",
        "user__first_name",
        "user__last_name",
    ]

class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = "profiles.add_studentprofile"
    form_class = StudentCreateForm
    template_name = "profiles/student/create.html"
    success_url = reverse_lazy("profiles:student_list")
    raise_exception = True

    @transaction.atomic
    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            email=form.cleaned_data["email"],
        )
        group = Group.objects.get(
            name=STUDENT_GROUP
        )
        user.groups.add(group)
        StudentProfile.objects.create(
            user=user,
            student_number=form.cleaned_data["student_number"],
            initial_enrollment_date=form.cleaned_data["initial_enrollment_date"],
        )

        return super().form_valid(form)

class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "profiles.change_studentprofile"
    model = StudentProfile
    form_class = StudentUpdateForm
    template_name = "profiles/student/update.html"
    success_url = reverse_lazy("profiles:student_list")
    raise_exception = True

class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "profiles.delete_studentprofile"
    model = StudentProfile
    template_name = "profiles/student/delete.html"
    success_url = reverse_lazy("profiles:student_list")
    raise_exception = True

    def form_valid(self, form):
        user = self.object.user
        response = super().form_valid(form)
        user.delete()
        return response

class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "profiles.view_studentprofile"
    model = StudentProfile
    template_name = "profiles/student/detail.html"
    context_object_name = "student"
    raise_exception = True