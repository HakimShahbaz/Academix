from django.conf import settings
from django.db import models

class TeacherProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='teacher_profile',
    )
    teacher_number = models.CharField(
        max_length=50,
        unique=True,
    )
    hire_date = models.DateField()

    class Meta:
        ordering = ["teacher_number"]
        verbose_name= "Teacher Profile"
        verbose_name_plural = "Teacher Profiles"

    def __str__(self):
        return f"{self.teacher_number} - {self.user.username}"