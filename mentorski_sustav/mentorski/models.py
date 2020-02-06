from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    MENTOR, STUDENT, NONE, REDOVNI, IZVANREDNI = 'mentor', 'student', 'none', 'redovni', 'izvanredni'
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

# SCAFFOLDED

class Predmeti(models.Model):
    ime = models.CharField(max_length=255)
    kod = models.CharField(unique=True, max_length=16)
    program = models.TextField()
    bodovi = models.IntegerField()
    sem_redovni = models.IntegerField()
    sem_izvanredni = models.IntegerField()
    NE,DA = 'ne','da'
    izborni_choices = (
        (NE, 'ne'),
        (DA, 'da'),
    )
    izborni = models.CharField(
        max_length=2,
        choices=izborni_choices,
        default=NE
    )

    class Meta:
        db_table = 'predmeti'

    def __str__(self):
        return self.kod


class Upisi(models.Model):
    student = models.ForeignKey(CustomUser, models.CASCADE)
    predmet = models.ForeignKey(Predmeti, models.CASCADE)
    status = models.CharField(max_length=64)

    class Meta:
        db_table = 'upisi'