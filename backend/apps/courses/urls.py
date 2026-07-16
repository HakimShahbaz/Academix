from django.urls import path

from .views import CourseDetailView, CourseDeleteView, CourseListView, CourseCreateView, CourseUpdateView
from .views import SectionDetailView, SectionDeleteView, SectionListView, SectionUpdateView, SectionCreateView

app_name = "courses"

urlpatterns = [
    path(
        "",
        CourseListView.as_view(),
        name="course_list"
    ),
    path(
        "create/",
        CourseCreateView.as_view(),
        name="course_create"
    ),
    path(
        "<int:pk>/edit/",
        CourseUpdateView.as_view(),
        name="course_update"
    ),
    path(
        "<int:pk>/delete/",
        CourseDeleteView.as_view(),
        name="course_delete"
    ),
    path(
        "<int:pk>/",
        CourseDetailView.as_view(),
        name="course_detail"
    ),

    path(
        "sections/",
        SectionListView.as_view(),
        name="section_list"
    ),
    path(
        "sections/create/",
        SectionCreateView.as_view(),
        name="section_create"
    ),
    path(
        "sections/<int:pk>/edit/",
        SectionUpdateView.as_view(),
        name="section_update"
    ),
    path(
        "sections/<int:pk>/delete/",
        SectionDeleteView.as_view(),
        name="section_delete"
    ),
    path(
        "sections/<int:pk>/",
        SectionDetailView.as_view(),
        name="section_detail"
    ),
]