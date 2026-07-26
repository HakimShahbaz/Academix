from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from apps.exams.models import Exam
from apps.exams.forms import ExamCreateForm, ExamUpdateForm

class ExamListView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = "exams/exam/list.html"
    context_object_name = "exams"
    paginate_by = 20

class ExamDetailView(LoginRequiredMixin, DetailView):
    model = Exam
    template_name = "exams/exam/detail.html"
    context_object_name = "exam"

class ExamCreateView(LoginRequiredMixin, CreateView):
    model = Exam
    form_class = ExamCreateForm
    template_name = "exams/exam/create.html"
    success_url = reverse_lazy('exams:exam_list')

class ExamUpdateView(LoginRequiredMixin, UpdateView):
    model = Exam
    form_class = ExamUpdateForm
    template_name = "exams/exam/update.html"
    success_url = reverse_lazy('exams:exam_list')

class ExamDeleteView(LoginRequiredMixin, DeleteView):
    model = Exam
    template_name = "exams/exam/delete.html"
    success_url = reverse_lazy('exams:exam_list')

