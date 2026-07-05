from django.conf import settings
from django.db import models

class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile',
    )
    student_number = models.CharField(
        max_length=50,
        unique=True,
    )
    initial_enrollment_date = models.DateField()

    class Meta:
        ordering = ['student_number']
        verbose_name = 'Student Profile'
        verbose_name_plural = 'Student Profiles'

    def __str__(self):
        return f"{self.student_number} - {self.user.username}"