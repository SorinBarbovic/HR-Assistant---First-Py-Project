from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    task_number = models.PositiveBigIntegerField()
    task_name = models.CharField (max_length=60)
    task_description = models.CharField (max_length=180)
    task_category = models.CharField (max_length=60)
    task_status = models.CharField (max_length=60)
    task_created_date = models.DateTimeField (default=datetime.now)
    task_due_date = models.DateTimeField (default=datetime.now)
    task_completed_date = models.DateTimeField (null=True)
    task_comment = models.CharField (max_length=180, null=True)
    # task_duration = models.DurationField()

    def __str__(self):
        return f'To Do: {self.task_name}'

