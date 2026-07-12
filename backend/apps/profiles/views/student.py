from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.profiles.models import StudentProfile


class StudentListView(LoginRequiredMixin,ListView):
    model = StudentProfile
    template_name = "profiles/student/list.html"
    context_object_name = "students"
    paginate_by = 20