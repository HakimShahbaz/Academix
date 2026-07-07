from django.db import models

from apps.profiles.models import StudentProfile
from apps.courses.models import Section


class Enrollment(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        DROPPED = "dropped", "Dropped"
        COMPLETED = "completed", "Completed"

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.PROTECT,
        related_name="enrollments",
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.PROTECT,
        related_name="enrollments",
    )
    enrolled_at = models.DateField(
        auto_now_add=True,
    )
    status = models.CharField(
        max_length=20,
        choices=Status,
        default=Status.ACTIVE,
    )

    class Meta:
        ordering = ["-enrolled_at"]
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

        constraints = [
            models.UniqueConstraint(
                fields=["student", "section"],
                name="unique_student_section",
            )
        ]

    def __str__(self):
        return f"{self.student.student_number} - {self.section.code}"