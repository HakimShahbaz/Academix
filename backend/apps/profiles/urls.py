from django.urls import path
from .views import (
    StudentListView, StudentCreateView, StudentUpdateView,
    StudentDetailView, StudentDeleteView
)
from .views import (
    TeacherListView, TeacherDeleteView, TeacherCreateView,
    TeacherUpdateView, TeacherDetailView
)

app_name = "profiles"

urlpatterns = [
    path(
        "students/",
        StudentListView.as_view(),
        name="student_list",
    ),
    path(
        "students/create/",
        StudentCreateView.as_view(),
        name="student_create",
    ),
    path(
        "students/<int:pk>/edit/",
        StudentUpdateView.as_view(),
        name="student_update",
    ),
    path(
        "students/<int:pk>/delete/",
        StudentDeleteView.as_view(),
        name="student_delete",
    ),
    path(
        "students/<int:pk>/",
        StudentDetailView.as_view(),
        name="student_detail",
    ),

    path(
        "teachers/",
        TeacherListView.as_view(),
        name="teacher_list",
    ),
    path(
        "teachers/create/",
        TeacherCreateView.as_view(),
        name="teacher_create",
    ),
    path(
        "teachers/<int:pk>/edit/",
        TeacherUpdateView.as_view(),
        name="teacher_update",
    ),
    path(
        "teachers/<int:pk>/delete/",
        TeacherDeleteView.as_view(),
        name="teacher_delete",
    ),
    path(
        "teachers/<int:pk>/",
        TeacherDetailView.as_view(),
        name="teacher_detail",
    ),
]