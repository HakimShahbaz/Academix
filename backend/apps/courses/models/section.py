from django.db import models

from .course import Course
from apps.profiles.models import TeacherProfile


class Section(models.Model):
    code = models.CharField(
        max_length=20,
        unique=True
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name='sections',
    )
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.PROTECT,
        related_name='sections',
    )
    capacity = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ['code']
        verbose_name='Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return f"{self.code} - {self.course}"