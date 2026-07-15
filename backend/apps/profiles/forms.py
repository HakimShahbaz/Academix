from django import forms

from apps.profiles.models import StudentProfile
from apps.profiles.models import TeacherProfile
from apps.profiles.models import EmployeeProfile

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile

        fields = [
            "user",
            "student_number",
            "initial_enrollment_date",
        ]

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile

        fields = [
            "user",
            "student_number",
            "initial_enrollment_date",
        ]

class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile

        fields = [
            "user",
            "teacher_number",
            "hire_date",
        ]

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = [
            "user",
            "teacher_number",
            "hire_date",
        ]

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = [
            "user",
            "employee_number",
            "hire_date",
        ]

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = [
            "user",
            "employee_number",
            "hire_date",
        ]