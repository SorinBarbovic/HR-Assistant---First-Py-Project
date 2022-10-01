from django.contrib import admin
from .models import Task, Holiday, Shopping

# Register your models here.
admin.site.register(Task)
admin.site.register(Holiday)
admin.site.register(Shopping)