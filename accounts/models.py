from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics and Communication'),
        ('EEE', 'Electrical and Electronics'),
        ('MECH', 'Mechanical'),
        ('CIVIL', 'Civil'),
        ('OTHER', 'Other'),
    ]

    YEAR_CHOICES = [
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES)

    def __str__(self):
        return self.user.username
