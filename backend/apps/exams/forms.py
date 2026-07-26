from django.forms import ModelForm

from .models import Exam, Grade

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

class GradeCreateForm(ModelForm):
    class Meta:
        model = Grade
        fields = [
            "enrollment",
            "exam",
            "score",
        ]

class GradeUpdateForm(ModelForm):
    class Meta:
        model = Grade
        fields = [
            "enrollment",
            "exam",
            "score",
        ]