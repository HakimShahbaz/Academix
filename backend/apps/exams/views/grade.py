from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.core.mixins import SearchableListViewMixin
from django.urls import reverse_lazy
from django.contrib import messages

from apps.exams.models import Grade
from apps.exams.forms import GradeCreateForm, GradeUpdateForm

class GradeListView(LoginRequiredMixin, PermissionRequiredMixin,SearchableListViewMixin, ListView):
    permission_required = "exams.view_grade"
    queryset = Grade.objects.select_related(
        "enrollment",
        "enrollment__student",
        "enrollment__student__user",
        "exam",
    )
    context_object_name = 'grades'
    template_name = "exams/grade/list.html"
    paginate_by = 20
    raise_exception = True

    search_fields = [
        "enrollment__student__student_number",
        "enrollment__student__user__username",
        "enrollment__student__user__first_name",
        "enrollment__student__user__last_name",
        "exam__title",
        "exam__section__code",
        "score",
    ]

class GradeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "exams.view_grade"
    queryset = Grade.objects.select_related(
        "enrollment",
        "enrollment__student",
        "enrollment__student__user",
        "exam",
    )
    context_object_name = 'grade'
    template_name = "exams/grade/detail.html"
    raise_exception = True

class GradeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "exams.add_grade"
    model = Grade
    form_class = GradeCreateForm
    template_name = "exams/grade/create.html"
    success_url = reverse_lazy('exams:grade_list')
    raise_exception = True

    def form_valid(self, form):
        messages.success(
            self.request,
            "Grade created successfully!"
        )

        return super().form_valid(form)

class GradeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "exams.change_grade"
    model = Grade
    form_class = GradeUpdateForm
    template_name = "exams/grade/update.html"
    success_url = reverse_lazy('exams:grade_list')
    raise_exception = True

    def form_valid(self, form):
        messages.success(
            self.request,
            "Grade updated successfully!"
        )

        return super().form_valid(form)

class GradeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "exams.delete_grade"
    model = Grade
    template_name = "exams/grade/delete.html"
    success_url = reverse_lazy('exams:grade_list')
    raise_exception = True

    def form_valid(self, form):
        messages.success(
            self.request,
            "Grade deleted successfully!"
        )

        return super().form_valid(form)
