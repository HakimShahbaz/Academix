from django.core.exceptions import ValidationError
from django.db import models
from apps.courses.models import Section

class Exam(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.PROTECT,
        related_name="exams",
    )
    title = models.CharField(
        max_length=100,
    )
    exam_date = models.DateField()
    maximum_score = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-exam_date"]

        verbose_name = "Exam"
        verbose_name_plural = "Exams"

    def clean(self):
        super().clean()

        if self.maximum_score <= 0:
            raise ValidationError({
                "maximum_score": "Maximum Score must be greater than 0"
            })

    def __str__(self):
        return f"{self.section.code} - {self.title}"