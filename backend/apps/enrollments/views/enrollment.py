from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.core.mixins import SearchableListViewMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from apps.enrollments.models import Enrollment
from apps.enrollments.forms import EnrollmentCreateForm, EnrollmentUpdateForm

class EnrollmentListView(LoginRequiredMixin, PermissionRequiredMixin,SearchableListViewMixin, ListView):
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

    search_fields = [
        "student__student_number",
        "student__user__first_name",
        "student__user__last_name",
        "student__user__username",
        "section__code",
        "section__course__title",
    ]

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

    def form_valid(self, form):
        messages.success(
            self.request,
            "Enrollment created successfully!"
        )

        return super().form_valid(form)

class EnrollmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "enrollments.change_enrollment"
    model = Enrollment
    form_class = EnrollmentUpdateForm
    template_name = "enrollments/enrollment/update.html"
    success_url = reverse_lazy('enrollments:enrollment_list')
    raise_exception = True

    def form_valid(self, form):
        messages.success(
            self.request,
            "Enrollment updated successfully!"
        )

        return super().form_valid(form)

class EnrollmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "enrollments.delete_enrollment"
    model = Enrollment
    template_name = "enrollments/enrollment/delete.html"
    success_url = reverse_lazy('enrollments:enrollment_list')
    raise_exception = True

    def form_valid(self, form):
        messages.success(
            self.request,
            "Enrollment deleted successfully!"
        )

        return super().form_valid(form)