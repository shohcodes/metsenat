from django.db import models


class StudentEducationType(models.TextChoices):
    bachelor = ('bachelor', 'Bakalavr')
    master = ('master', 'Magistr')
