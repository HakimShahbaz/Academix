from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from apps.exams.models import Grade
from apps.exams.forms import GradeCreateForm, GradeUpdateForm

class GradeListView(LoginRequiredMixin, ListView):
    queryset = Grade.objects.select_related(
        "enrollment",
        "enrollment__student",
        "enrollment__student__user",
        "exam",
    )
    context_object_name = 'grades'
    template_name = "exams/grade/list.html"
    paginate_by = 20

class GradeDetailView(LoginRequiredMixin, DetailView):
    queryset = Grade.objects.select_related(
        "enrollment",
        "enrollment__student",
        "enrollment__student__user",
        "exam",
    )
    context_object_name = 'grade'
    template_name = "exams/grade/detail.html"

class GradeCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    form_class = GradeCreateForm
    template_name = "exams/grade/create.html"
    success_url = reverse_lazy('exams:grade_list')

class GradeUpdateView(LoginRequiredMixin, UpdateView):
    model = Grade
    form_class = GradeUpdateForm
    template_name = "exams/grade/update.html"
    success_url = reverse_lazy('exams:grade_list')

class GradeDeleteView(LoginRequiredMixin, DeleteView):
    model = Grade
    template_name = "exams/grade/delete.html"
    success_url = reverse_lazy('exams:grade_list')

