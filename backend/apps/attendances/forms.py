from django.forms import ModelForm
from .models import Attendance

class AttendanceCreateForm(ModelForm):
    class Meta:
        model = Attendance
        fields = [
            "enrollment",
            "date",
            "status",
        ]

class AttendanceUpdateForm(ModelForm):
    class Meta:
        model = Attendance
        fields = [
            "enrollment",
            "date",
            "status",
        ]