from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.attendances.models import Attendance
from apps.courses.models import Course, Section
from apps.exams.models import Exam, Grade
from apps.enrollments.models import Enrollment
from apps.profiles.models import StudentProfile, TeacherProfile, EmployeeProfile


@login_required()
def dashboard(request):
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
    }

    return render(request, "core/dashboard.html", context)