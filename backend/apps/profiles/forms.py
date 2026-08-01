from django import forms

from apps.profiles.models import StudentProfile
from apps.profiles.models import TeacherProfile
from apps.profiles.models import EmployeeProfile

class StudentCreateForm(forms.Form):
    username = forms.CharField(
        max_length=100,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
    first_name = forms.CharField(
        max_length=100,
        required=False,
    )
    last_name = forms.CharField(
        max_length=100,
        required=False,
    )
    email = forms.EmailField(
        required=False,
    )
    student_number = forms.CharField(
        max_length=50,
    )
    initial_enrollment_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date"},
        ),
    )

    def clean_username(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username already exists."
            )
        return username

    def clean_student_number(self):
        from apps.profiles.models import StudentProfile

        student_number = self.cleaned_data["student_number"]

        if StudentProfile.objects.filter(student_number=student_number).exists():
            raise forms.ValidationError(
                "Student number already exists."
            )

        return student_number


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile

        fields = [
            "user",
            "student_number",
            "initial_enrollment_date",
        ]

class TeacherCreateForm(forms.Form):
    username = forms.CharField(
        max_length=100,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
    first_name = forms.CharField(
        max_length=100,
        required=False,
    )
    last_name = forms.CharField(
        max_length=100,
        required=False,
    )
    email = forms.EmailField(
        required=False,
    )
    teacher_number = forms.CharField(
        max_length=50,
    )
    hire_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date"},
        )
    )

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = [
            "user",
            "teacher_number",
            "hire_date",
        ]

class EmployeeCreateForm(forms.Form):
    username = forms.CharField(
        max_length=100,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
    first_name = forms.CharField(
        max_length=100,
        required=False,
    )
    last_name = forms.CharField(
        max_length=100,
        required=False,
    )
    email = forms.EmailField(
        required=False,
    )
    employee_number = forms.CharField(
        max_length=50,
    )
    hire_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date"},
        )
    )

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = [
            "user",
            "employee_number",
            "hire_date",
        ]