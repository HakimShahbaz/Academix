from django.db import models

class Course(models.Model):
    code = models.CharField(
        max_length=20,
        unique=True,
    )
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ['code']
        verbose_name='Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f"{self.code} - {self.title}"
