from django.db import models

class TaskLabel(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TaskStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Task(models.Model):
    number = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=2045)
    description = models.TextField()
    status = models.ForeignKey(TaskStatus, default=None, on_delete=models.DO_NOTHING)
    labels = models.ManyToManyField(TaskLabel, blank=True, related_name="labels")
    child_of = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number

