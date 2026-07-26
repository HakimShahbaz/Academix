from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.courses.models import Section
from apps.courses.forms import SectionCreateForm, SectionUpdateForm

class SectionListView(LoginRequiredMixin, ListView):
    queryset = Section.objects.select_related(
        "course",
        "teacher",
    )
    context_object_name = "sections"
    template_name = "courses/section/list.html"
    paginate_by = 20

class SectionCreateView(LoginRequiredMixin, CreateView):
    model = Section
    form_class = SectionCreateForm
    template_name = "courses/section/create.html"
    success_url = reverse_lazy("courses:section_list")

class SectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Section
    form_class = SectionUpdateForm
    template_name = "courses/section/update.html"
    success_url = reverse_lazy("courses:section_list")

class SectionDeleteView(LoginRequiredMixin, DeleteView):
    model = Section
    template_name = "courses/section/delete.html"
    success_url = reverse_lazy("courses:section_list")

class SectionDetailView(LoginRequiredMixin, DetailView):
    queryset = Section.objects.select_related(
        "course",
        "teacher"
    )
    template_name = "courses/section/detail.html"
    context_object_name = "section"