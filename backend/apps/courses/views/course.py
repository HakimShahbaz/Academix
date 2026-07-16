from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.courses.models import Course
from apps.courses.forms import CourseCreateForm, CourseUpdateForm

class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = "courses/course/list.html"
    paginate_by = 20

class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    context_object_name = 'course'
    template_name = "courses/course/detail.html"

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseCreateForm
    template_name = "courses/course/create.html"
    success_url = reverse_lazy("courses:course_list")

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseUpdateForm
    template_name = "courses/course/update.html"
    success_url = reverse_lazy("courses:course_list")

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = "courses/course/delete.html"
    success_url = reverse_lazy("courses:course_list")

