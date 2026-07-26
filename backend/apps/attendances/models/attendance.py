from django.db import models

from apps.enrollments.models import Enrollment
from django.core.exceptions import ValidationError
from django.utils import timezone

class Attendance(models.Model):

    class Status(models.TextChoices):
        PRESENT = 'present', 'Present'
        ABSENT = 'absent', 'Absent'
        LATE = 'late', 'Late'

    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.PROTECT,
        related_name='attendances',
    )
    date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=Status,
        default=Status.PRESENT,
    )
    class Meta:
        ordering = ['-date',]
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

        constraints = [
            models.UniqueConstraint(
                fields=['enrollment', 'date'],
                name='unique_attendance_per_day',
            )
        ]

    def clean(self):
        super().clean()

        if self.date > timezone.now().date():
            raise ValidationError({
                "date": "Attendance date cannot be in the future"
            })

    def __str__(self):
        return (f'{self.enrollment.student.student_number} | '
                f'{self.date} | {self.status}')
