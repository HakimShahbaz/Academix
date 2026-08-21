from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.core.mixins import SearchableListViewMixin, SortableListViewMixin
from django.urls import reverse_lazy
from django.contrib import messages

from apps.exams.models import Exam
from apps.exams.forms import ExamCreateForm, ExamUpdateForm

class ExamListView(LoginRequiredMixin, PermissionRequiredMixin, SearchableListViewMixin,SortableListViewMixin, ListView):
    permission_required = 'exams.view_exam'
    queryset = Exam.objects.select_related(
        "section",
        "section__course",
    )
    template_name = "exams/exam/list.html"
    context_object_name = "exams"
    paginate_by = 20
    raise_exception = True

    search_fields = [
        "title",
        "section__code",
        "section__course__title",
    ]

    sort_fields = [
        "title",
        "section__code",
        "section__course__title",
        "exam_date",
        "maximum_score",
        "is_active",
    ]

class ExamDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'exams.view_exam'
    queryset = Exam.objects.select_related(
        "section",
        "section__course",
    )
    template_name = "exams/exam/detail.html"
    context_object_name = "exam"
    raise_exception = True

class ExamCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'exams.add_exam'
    model = Exam
    form_class = ExamCreateForm
    template_name = "exams/exam/create.html"
    success_url = reverse_lazy('exams:exam_list')
    raise_exception = True

    def form_valid(self, form):
        messages.success(
            self.request,
            "Exam created successfully!"
        )

        return super().form_valid(form)

class ExamUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'exams.change_exam'
    model = Exam
    form_class = ExamUpdateForm
    template_name = "exams/exam/update.html"
    success_url = reverse_lazy('exams:exam_list')
    raise_exception = True

    def form_valid(self, form):
        messages.success(
            self.request,
            "Exam updated successfully!"
        )

        return super().form_valid(form)

class ExamDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'exams.delete_exam'
    model = Exam
    template_name = "exams/exam/delete.html"
    success_url = reverse_lazy('exams:exam_list')
    raise_exception = True

    def form_valid(self, form):
        messages.success(
            self.request,
            "Exam deleted successfully!"
        )

        return super().form_valid(form)

