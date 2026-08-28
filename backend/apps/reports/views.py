from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from apps.profiles.models import StudentProfile
from apps.profiles.models import TeacherProfile
from apps.profiles.models import EmployeeProfile
from apps.attendances.models import Attendance
from apps.exams.models import Grade
from apps.courses.models import Section


class StudentReportView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    TemplateView,
):
    permission_required = "profiles.view_studentprofile"
    template_name = "reports/student/detail.html"
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = get_object_or_404(
            StudentProfile.objects.select_related("user"),
            pk=self.kwargs["pk"],
        )

        enrollments = (
            student.enrollments
            .select_related(
                "section",
                "section__course",
            )
            .all()
        )

        attendances = (
            Attendance.objects
            .filter(enrollment__student=student)
            .select_related(
                "enrollment",
                "enrollment__section",
                "enrollment__section__course",
            )
        )

        grades = (
            Grade.objects
            .filter(enrollment__student=student)
            .select_related(
                "enrollment",
                "enrollment__section",
                "enrollment__section__course",
                "exam",
            )
        )

        context["student"] = student
        context["enrollments"] = enrollments
        context["attendances"] = attendances
        context["grades"] = grades

        return context

class TeacherReportView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    TemplateView,
):
    permission_required = "profiles.view_teacherprofile"
    template_name = "reports/teacher/detail.html"
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teacher = get_object_or_404(
            TeacherProfile.objects.select_related("user"),
            pk=self.kwargs["pk"],
        )

        sections = (
            Section.objects
            .filter(teacher=teacher)
            .select_related("course")
        )

        context["teacher"] = teacher
        context["sections"] = sections

        return context

class EmployeeReportView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    TemplateView,
):
    permission_required = "profiles.view_employeeprofile"
    template_name = "reports/employee/detail.html"
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        employee = get_object_or_404(
            EmployeeProfile.objects.select_related("user"),
            pk=self.kwargs["pk"],
        )

        context["employee"] = employee

        return context