from django.forms import ModelForm

from .models import Exam

class ExamCreateForm(ModelForm):
    class Meta:
        model = Exam
        fields = [
            "section",
            "title",
            "exam_date",
            "maximum_score",
            "is_active",
        ]

class ExamUpdateForm(ModelForm):
    class Meta:
        model = Exam
        fields = [
            "section",
            "title",
            "exam_date",
            "maximum_score",
            "is_active",
        ]