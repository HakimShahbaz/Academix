from django import forms

from apps.courses.models import Course, Section

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class SectionCreateForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = [
            "code",
            "course",
            "teacher",
            "capacity",
            "start_date",
            "end_date",
            "is_active",
        ]

class SectionUpdateForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = [
            "code",
            "course",
            "teacher",
            "capacity",
            "start_date",
            "end_date",
            "is_active",
        ]