# Create your models here.
from django.db import models

class Task(models.Model):
    data = models.TextField()  # Store any data related to the task
    processed = models.BooleanField(default=False)  # Indicates whether the task has been processed