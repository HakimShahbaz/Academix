from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from apps.profiles.models import StudentProfile
from apps.profiles.forms import StudentCreateForm, StudentUpdateForm

class StudentListView(LoginRequiredMixin,ListView):
    model = StudentProfile
    template_name = "profiles/student/list.html"
    context_object_name = "students"
    paginate_by = 20

class StudentCreateView(LoginRequiredMixin,CreateView):
    model = StudentProfile
    form_class = StudentCreateForm
    template_name = "profiles/student/create.html"
    success_url = reverse_lazy("profiles:student_list")

class StudentUpdateView(LoginRequiredMixin,UpdateView):
    model = StudentProfile
    form_class = StudentUpdateForm
    template_name = "profiles/student/update.html"
    success_url = reverse_lazy("profiles:student_list")

class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model = StudentProfile
    template_name = "profiles/student/delete.html"
    success_url = reverse_lazy("profiles:student_list")

class StudentDetailView(LoginRequiredMixin,DetailView):
    model = StudentProfile
    template_name = "profiles/student/detail.html"
    context_object_name = "student"