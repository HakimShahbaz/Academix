from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.core.mixins import SearchableListViewMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.courses.models import Course
from apps.courses.forms import CourseCreateForm, CourseUpdateForm

class CourseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "courses.view_course"
    model = Course
    context_object_name = 'courses'
    template_name = "courses/course/list.html"
    paginate_by = 20
    raise_exception = True

    search_fields = [
        "code",
        "title",
    ]

class CourseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "courses.view_course"
    model = Course
    context_object_name = 'course'
    template_name = "courses/course/detail.html"
    raise_exception = True

class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "courses.add_course"
    model = Course
    form_class = CourseCreateForm
    template_name = "courses/course/create.html"
    success_url = reverse_lazy("courses:course_list")
    raise_exception = True

class CourseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "courses.change_course"
    model = Course
    form_class = CourseUpdateForm
    template_name = "courses/course/update.html"
    success_url = reverse_lazy("courses:course_list")
    raise_exception = True

class CourseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "courses.delete_course"
    model = Course
    template_name = "courses/course/delete.html"
    success_url = reverse_lazy("courses:course_list")
    raise_exception = True

