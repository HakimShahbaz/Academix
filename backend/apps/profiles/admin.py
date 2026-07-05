from django.contrib import admin
from .models import StudentProfile

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