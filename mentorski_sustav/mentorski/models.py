from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    MENTOR = 'mentor'
    STUDENT = 'student'
    NONE = 'none'
    REDOVNI = 'redovni'
    IZVANREDNI = 'izvanredni'
    role_choices = (
        (MENTOR, 'mentor'),
        (STUDENT, 'student')
    )
    role = models.CharField(
        max_length=64,
        choices=role_choices,
        default=STUDENT
    )
    status_choices = (
        (NONE, 'none'),
        (REDOVNI, 'redovni'),
        (IZVANREDNI, 'izvanredni')

    )
    status = models.CharField(
        max_length=64,
        choices=status_choices,
        default=REDOVNI
    )

    def __str__(self):
            return self.username