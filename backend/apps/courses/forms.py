from django import forms

from apps.courses.models import Course

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"