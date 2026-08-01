from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.enrollments.models import Enrollment
from apps.enrollments.forms import EnrollmentCreateForm, EnrollmentUpdateForm

class EnrollmentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "enrollments.view_enrollment"
    queryset = Enrollment.objects.select_related(
        "student",
        "student__user",
        "section",
        "section__course",
    )
    context_object_name = 'enrollments'
    template_name = "enrollments/enrollment/list.html"
    paginate_by = 20
    raise_exception = True

class EnrollmentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "enrollments.view_enrollment"
    queryset = Enrollment.objects.select_related(
        "student",
        "student__user",
        "section",
        "section__course",
    )
    context_object_name = 'enrollment'
    template_name = "enrollments/enrollment/detail.html"
    raise_exception = True

class EnrollmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "enrollments.add_enrollment"
    model = Enrollment
    form_class = EnrollmentCreateForm
    template_name = "enrollments/enrollment/create.html"
    success_url = reverse_lazy('enrollments:enrollment_list')
    raise_exception = True

class EnrollmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "enrollments.change_enrollment"
    model = Enrollment
    form_class = EnrollmentUpdateForm
    template_name = "enrollments/enrollment/update.html"
    success_url = reverse_lazy('enrollments:enrollment_list')
    raise_exception = True

class EnrollmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "enrollments.delete_enrollment"
    model = Enrollment
    template_name = "enrollments/enrollment/delete.html"
    success_url = reverse_lazy('enrollments:enrollment_list')
    raise_exception = True