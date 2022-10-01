import django_filters
from .models import *

class TaskFilter(django_filters.filterset):
    class Meta:
        model = Task
        fields = 'task_name', 'task_description'
        