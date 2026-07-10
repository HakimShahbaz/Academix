from django.db import models

from apps.enrollments.models import Enrollment

from apps.exams.models import Exam


class Grade(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.PROTECT,
        related_name="grades",
    )
    exam = models.ForeignKey(
        Exam,
        on_delete=models.PROTECT,
        related_name="grades",
    )
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    class Meta:
        ordering = ["exam"]
        verbose_name = "Grade"
        verbose_name_plural = "Grades"

        constraints = [
            models.UniqueConstraint(
                fields=["enrollment", "exam"],
                name="unique_grade_per_exam",
            )
        ]

    def  __str__(self):
        return (
            f"{self.enrollment.student.student_number} | {self.exam.title} |"
            f"{self.score}"
        )
