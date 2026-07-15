from .student import (
    StudentListView, StudentCreateView, StudentUpdateView,
    StudentDetailView, StudentDeleteView
)

from .teacher import (
    TeacherListView, TeacherCreateView, TeacherDeleteView,
    TeacherDetailView, TeacherUpdateView
)

__all__ = [
    "StudentListView",
    "StudentCreateView",
    "StudentUpdateView",
    "StudentDeleteView",
    "StudentDetailView",

    "TeacherListView",
    "TeacherCreateView",
    "TeacherUpdateView",
    "TeacherDetailView",
    "TeacherDeleteView"
]