# Create your models here.
from django.db import models

class Task(models.Model):
    data = models.TextField()  # Store any data related to the task
    processed = models.BooleanField(default=False)  # Indicates whether the task has been processed
    status = models.IntegerField(db_column='STATUS', blank=True, null=True) # Failed Status of the task after 1 sec of processing

    class Meta:
        managed = False
        db_table = 'demo_app_task'
