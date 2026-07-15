from .student import (
    StudentListView, StudentCreateView, StudentUpdateView,
    StudentDetailView, StudentDeleteView
)

from .teacher import (
    TeacherListView, TeacherCreateView, TeacherDeleteView,
    TeacherDetailView, TeacherUpdateView
)

from .employee import (
    EmployeeListView, EmployeeCreateView, EmployeeDeleteView,
    EmployeeUpdateView, EmployeeDetailView
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
    "TeacherDeleteView",

    "EmployeeListView",
    "EmployeeCreateView",
    "EmployeeUpdateView",
    "EmployeeDetailView",
    "EmployeeDeleteView",
]