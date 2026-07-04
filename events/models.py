from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):

    CATEGORY_CHOICES = [
        ('TECH', 'Technical'),
        ('CULT', 'Cultural'),
        ('SPORT', 'Sports'),
        ('WORKSHOP', 'Workshop'),
        ('SEMINAR', 'Seminar'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('COMPLETED', 'Completed'),
    ]

    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='organized_events'
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    venue = models.CharField(max_length=200)

    event_date = models.DateField()
    event_time = models.TimeField()

    registration_deadline = models.DateTimeField()

    capacity = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title