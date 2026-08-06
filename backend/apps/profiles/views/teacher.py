from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.core.mixins import SearchableListViewMixin
from django.contrib.auth.models import Group
from django.db import transaction
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from apps.profiles.models import TeacherProfile
from apps.profiles.forms import TeacherUpdateForm, TeacherCreateForm
from apps.accounts.constants import TEACHER_GROUP

User = get_user_model()

class TeacherListView(LoginRequiredMixin, PermissionRequiredMixin, SearchableListViewMixin, ListView):
    permission_required = "profiles.view_teacherprofile"
    model = TeacherProfile
    context_object_name = "teachers"
    template_name = "profiles/teacher/list.html"
    paginate_by = 20
    raise_exception = True

    search_fields = [
        "teacher_number",
        "user__username",
        "user__first_name",
        "user__last_name",
    ]

class TeacherDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "profiles.view_teacherprofile"
    model = TeacherProfile
    context_object_name = "teacher"
    template_name = "profiles/teacher/detail.html"
    raise_exception = True

class TeacherCreateView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = "profiles.add_teacherprofile"
    template_name = "profiles/teacher/create.html"
    form_class = TeacherCreateForm
    success_url = reverse_lazy("profiles:teacher_list")
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
            name=TEACHER_GROUP
        )
        user.groups.add(group)
        TeacherProfile.objects.create(
            user=user,
            teacher_number = form.cleaned_data["teacher_number"],
            hire_date = form.cleaned_data["hire_date"],
        )

        return super().form_valid(form)


class TeacherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "profiles.change_teacherprofile"
    model = TeacherProfile
    form_class = TeacherUpdateForm
    template_name = "profiles/teacher/update.html"
    success_url = reverse_lazy("profiles:teacher_list")
    raise_exception = True

class TeacherDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "profiles.delete_teacherprofile"
    model = TeacherProfile
    template_name = "profiles/teacher/delete.html"
    success_url = reverse_lazy("profiles:teacher_list")
    raise_exception = True

    def form_valid(self, form):
        user = self.object.user
        response = super().form_valid(form)
        user.delete()
        return response
