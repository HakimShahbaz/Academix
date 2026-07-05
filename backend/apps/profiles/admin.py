from django.contrib import admin
from .models import (
    StudentProfile, TeacherProfile, EmployeeProfile
)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "student_number",
        "user",
        "initial_enrollment_date")
    search_fields = (
        "student_number",
        "user__username",
        "user__first_name",
        "user__last_name",
    )
    ordering = ("student_number",)

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = (
        "teacher_number",
        "user",
        "hire_date")
    search_fields = (
        "teacher_number",
        "user__username",
        "user__first_name",
        "user__last_name",
    )
    ordering = ("teacher_number",)

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = (
        "employee_number",
        "user",
        "hire_date")
    search_fields = (
        "employee_number",
        "user__username",
        "user__first_name",
        "user__last_name",
    )
    ordering = ("employee_number",)