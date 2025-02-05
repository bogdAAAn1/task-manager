from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        related_name="workers",
        on_delete=models.SET_NULL,
        null=True
    )

    def get_absolute_url(self):
        return reverse("tasks:worker-detail", kwargs={"pk": self.pk})

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("High", "High"),
        ("Urgent", "Urgent"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default="Low"
    )
    task_type = models.ForeignKey(
        TaskType,
        related_name="tasks",
        on_delete=models.CASCADE
    )
    assignees = models.ManyToManyField(Worker, related_name="assigned_tasks")

    class Meta:
        ordering = ["is_completed", "-priority", "-deadline", ]
