from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.attendances.models import Attendance
from apps.attendances.forms import AttendanceCreateForm, AttendanceUpdateForm

class AttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = "attendances/attendance/list.html"
    context_object_name = "attendances"
    paginate_by = 20

class AttendanceDetailView(LoginRequiredMixin, DetailView):
    model = Attendance
    context_object_name = "attendance"
    template_name = "attendances/attendance/detail.html"

class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    form_class = AttendanceCreateForm
    template_name = "attendances/attendance/create.html"
    success_url = reverse_lazy("attendances:attendance_list")

class AttendanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Attendance
    form_class = AttendanceUpdateForm
    template_name = "attendances/attendance/update.html"
    success_url = reverse_lazy("attendances:attendance_list")

class AttendanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Attendance
    template_name = "attendances/attendance/delete.html"
    success_url = reverse_lazy("attendances:attendance_list")