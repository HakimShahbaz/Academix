from django.forms import ModelForm

from .models.enrollment import Enrollment

class EnrollmentCreateForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = [
            "student",
            "section",
            "status",
        ]

class EnrollmentUpdateForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = [
            "student",
            "section",
            "status",
        ]