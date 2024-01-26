from django.contrib import admin
from .models import Task, TaskStatus, TaskLabel

admin.site.register(Task)
admin.site.register(TaskStatus)
admin.site.register(TaskLabel)
