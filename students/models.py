from django.db import models

from core.models import TimeStampedModel
from students.choices import StudentEducationType


class Institute(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Institute'
        verbose_name_plural = 'Institutes'

    def __str__(self):
        return f"{self.name}"


class Student(TimeStampedModel):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    type = models.CharField(max_length=20, choices=StudentEducationType.choices)
    institute = models.ForeignKey(Institute, related_name='student_institute', on_delete=models.PROTECT)
    contract_amount = models.IntegerField()

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.full_name}"
