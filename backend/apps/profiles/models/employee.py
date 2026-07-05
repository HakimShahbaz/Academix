from django.conf import settings
from django.db import models

class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employee_profile',
    )
    employee_number = models.CharField(
        max_length=50,
        unique=True,
    )
    hire_date = models.DateField()

    class Meta:
        ordering = ['employee_number',]
        verbose_name='Employee Profile'
        verbose_name_plural = 'Employee Profiles'

    def __str__(self):
        return f"{self.employee_number} - {self.user.username}"