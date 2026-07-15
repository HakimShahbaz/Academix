from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.profiles.models import TeacherProfile
from apps.profiles.forms import TeacherUpdateForm, TeacherCreateForm

class TeacherListView(LoginRequiredMixin, ListView):
    model = TeacherProfile
    context_object_name = "teachers"
    template_name = "profiles/teacher/list.html"
    paginate_by = 20

class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = TeacherProfile
    context_object_name = "teacher"
    template_name = "profiles/teacher/detail.html"

class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = TeacherProfile
    template_name = "profiles/teacher/create.html"
    form_class = TeacherCreateForm
    success_url = reverse_lazy("profiles:teacher_list")

class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = TeacherProfile
    form_class = TeacherUpdateForm
    template_name = "profiles/teacher/update.html"
    success_url = reverse_lazy("profiles:teacher_list")

class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = TeacherProfile
    template_name = "profiles/teacher/delete.html"
    success_url = reverse_lazy("profiles:teacher_list")
