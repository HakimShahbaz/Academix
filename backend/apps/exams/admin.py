from django.contrib import admin
from .models import Exam, Grade


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass