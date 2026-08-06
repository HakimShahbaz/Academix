from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.core.mixins import SearchableListViewMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.courses.models import Section
from apps.courses.forms import SectionCreateForm, SectionUpdateForm

class SectionListView(LoginRequiredMixin, PermissionRequiredMixin,SearchableListViewMixin, ListView):
    permission_required = "courses.view_section"
    queryset = Section.objects.select_related(
        "course",
        "teacher",
    )
    context_object_name = "sections"
    template_name = "courses/section/list.html"
    paginate_by = 20
    raise_exception = True

    search_fields = [
        "code",
        "course__title",
        "teacher__teacher_number",
        "teacher__user__username",
        "teacher__user__first_name",
        "teacher__user__last_name",
    ]

class SectionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "courses.add_section"
    model = Section
    form_class = SectionCreateForm
    template_name = "courses/section/create.html"
    success_url = reverse_lazy("courses:section_list")
    raise_exception = True

class SectionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "courses.change_section"
    model = Section
    form_class = SectionUpdateForm
    template_name = "courses/section/update.html"
    success_url = reverse_lazy("courses:section_list")
    raise_exception = True

class SectionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "courses.delete_section"
    model = Section
    template_name = "courses/section/delete.html"
    success_url = reverse_lazy("courses:section_list")
    raise_exception = True

class SectionDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "courses.view_section"
    queryset = Section.objects.select_related(
        "course",
        "teacher"
    )
    template_name = "courses/section/detail.html"
    context_object_name = "section"
    raise_exception = True