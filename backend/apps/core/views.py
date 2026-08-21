from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from apps.attendances.models import Attendance
from apps.courses.models import Course, Section
from apps.exams.models import Exam, Grade
from apps.enrollments.models import Enrollment
from apps.profiles.models import StudentProfile, TeacherProfile, EmployeeProfile


@login_required()
def dashboard(request):

    recent_enrollments = Enrollment.objects.select_related(
        "student", "student__user", "section", "section__course"
    ).order_by("-enrolled_at")[:5]

    upcoming_exams = Exam.objects.select_related(
        "section", "section__course"
    ).filter(
        exam_date__gte=timezone.localdate(),
        is_active=True,
    ).order_by("exam_date")[:5]

    context = {
        "student_count": StudentProfile.objects.count(),
        "teacher_count": TeacherProfile.objects.count(),
        "employee_count": EmployeeProfile.objects.count(),
        "course_count": Course.objects.count(),
        "section_count": Section.objects.count(),
        "enrollment_count": Enrollment.objects.count(),
        "attendance_count": Attendance.objects.count(),
        "exam_count": Exam.objects.count(),
        "grades_count": Grade.objects.count(),

        "recent_enrollments": recent_enrollments,
        "upcoming_exams": upcoming_exams,
    }

    return render(request, "core/dashboard.html", context)