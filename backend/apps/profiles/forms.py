from django import forms

from apps.profiles.models import StudentProfile

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