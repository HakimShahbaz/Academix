from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.core.mixins import SearchableListViewMixin
from django.urls import reverse_lazy

from apps.exams.models import Exam
from apps.exams.forms import ExamCreateForm, ExamUpdateForm

class ExamListView(LoginRequiredMixin, PermissionRequiredMixin, SearchableListViewMixin, ListView):
    permission_required = 'exams.view_exam'
    model = Exam
    template_name = "exams/exam/list.html"
    context_object_name = "exams"
    paginate_by = 20
    raise_exception = True

    search_fields = [
        "title",
        "section__code",
    ]

class ExamDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'exams.view_exam'
    model = Exam
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

class ExamUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'exams.change_exam'
    model = Exam
    form_class = ExamUpdateForm
    template_name = "exams/exam/update.html"
    success_url = reverse_lazy('exams:exam_list')
    raise_exception = True

class ExamDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'exams.delete_exam'
    model = Exam
    template_name = "exams/exam/delete.html"
    success_url = reverse_lazy('exams:exam_list')
    raise_exception = True

