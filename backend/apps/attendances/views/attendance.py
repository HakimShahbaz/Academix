from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.attendances.models import Attendance
from apps.attendances.forms import AttendanceCreateForm, AttendanceUpdateForm

class AttendanceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    queryset = Attendance.objects.select_related(
        "enrollment",
        "enrollment__student",
        "enrollment__student__user",
        "enrollment__section",
        "enrollment__section__course",
    )
    permission_required = "attendances.view_attendance"
    template_name = "attendances/attendance/list.html"
    context_object_name = "attendances"
    paginate_by = 20
    raise_exception = True

class AttendanceDetailView(LoginRequiredMixin, PermissionRequiredMixin,  DetailView):
    queryset = Attendance.objects.select_related(
        "enrollment",
        "enrollment__student",
        "enrollment__student__user",
        "enrollment__section",
        "enrollment__section__course",
    )
    permission_required = "attendances.view_attendance"
    context_object_name = "attendance"
    template_name = "attendances/attendance/detail.html"
    raise_exception = True

class AttendanceCreateView(LoginRequiredMixin, PermissionRequiredMixin,  CreateView):
    model = Attendance
    permission_required = "attendances.add_attendance"
    form_class = AttendanceCreateForm
    template_name = "attendances/attendance/create.html"
    success_url = reverse_lazy("attendances:attendance_list")
    raise_exception = True

class AttendanceUpdateView(LoginRequiredMixin, PermissionRequiredMixin,  UpdateView):
    model = Attendance
    permission_required = "attendances.change_attendance"
    form_class = AttendanceUpdateForm
    template_name = "attendances/attendance/update.html"
    success_url = reverse_lazy("attendances:attendance_list")
    raise_exception = True

class AttendanceDeleteView(LoginRequiredMixin, PermissionRequiredMixin,  DeleteView):
    model = Attendance
    permission_required = "attendances.delete_attendance"
    template_name = "attendances/attendance/delete.html"
    success_url = reverse_lazy("attendances:attendance_list")
    raise_exception = True