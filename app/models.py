from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', "To Do"),
        ('in_progress', "In Progress"),
        ('done', "Done")
    ]
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ('medium', "Medium"),
        ('high', "High")
    ]


    title = models.CharField(max_length = 150)
    description = models.TextField()
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = "todo")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    creator = models.ForeignKey(User , on_delete=models.CASCADE, related_name='tusks', verbose_name="Author")
    due_date = models.DateField(null = True, blank = True)


    def __str__(self):
        return self.title

