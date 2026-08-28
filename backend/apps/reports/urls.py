from django.urls import path

from apps.reports import views


app_name = "reports"


urlpatterns = [
    path(
        "students/<int:pk>/",
        views.StudentReportView.as_view(),
        name="student_report",
    ),
    path(
        "teachers/<int:pk>/",
        views.TeacherReportView.as_view(),
        name="teacher_report",
    ),
    path(
        "employees/<int:pk>/",
        views.EmployeeReportView.as_view(),
        name="employee_report",
    ),
]