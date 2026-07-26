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

STUDENT_VIEWS = [
    "StudentListView",
    "StudentCreateView",
    "StudentUpdateView",
    "StudentDeleteView",
    "StudentDetailView",
]

TEACHER_VIEWS = [
    "TeacherListView",
    "TeacherCreateView",
    "TeacherUpdateView",
    "TeacherDetailView",
    "TeacherDeleteView",
]

EMPLOYEE_VIEWS = [
    "EmployeeListView",
    "EmployeeCreateView",
    "EmployeeUpdateView",
    "EmployeeDetailView",
    "EmployeeDeleteView",
]

__all__ = STUDENT_VIEWS + TEACHER_VIEWS + EMPLOYEE_VIEWS