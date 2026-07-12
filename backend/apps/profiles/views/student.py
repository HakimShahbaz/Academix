from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from apps.profiles.models import StudentProfile
from apps.profiles.forms import StudentCreateForm

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