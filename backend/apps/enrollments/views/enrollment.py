from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.enrollments.models import Enrollment
from apps.enrollments.forms import EnrollmentCreateForm, EnrollmentUpdateForm

class EnrollmentListView(LoginRequiredMixin, ListView):
    queryset = Enrollment.objects.select_related(
        "student",
        "student__user",
        "section",
        "section__course",
    )
    context_object_name = 'enrollments'
    template_name = "enrollments/enrollment/list.html"
    paginate_by = 20

class EnrollmentDetailView(LoginRequiredMixin, DetailView):
    queryset = Enrollment.objects.select_related(
        "student",
        "student__user",
        "section",
        "section__course",
    )
    context_object_name = 'enrollment'
    template_name = "enrollments/enrollment/detail.html"

class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    model = Enrollment
    form_class = EnrollmentCreateForm
    template_name = "enrollments/enrollment/create.html"
    success_url = reverse_lazy('enrollments:enrollment_list')

class EnrollmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Enrollment
    form_class = EnrollmentUpdateForm
    template_name = "enrollments/enrollment/update.html"
    success_url = reverse_lazy('enrollments:enrollment_list')

class EnrollmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Enrollment
    template_name = "enrollments/enrollment/delete.html"
    success_url = reverse_lazy('enrollments:enrollment_list')
