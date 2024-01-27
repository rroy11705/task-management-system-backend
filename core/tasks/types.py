import graphene
from graphene_django import DjangoObjectType
from .models import Task, TaskStatus, TaskLabel

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ("id", "number", "title", "description", "status", "labels", "child_of", "date_created")

class TaskStatusType(DjangoObjectType):
    class Meta:
        model = TaskStatus
        fields = ("id", "name", "description")

class TaskLabelType(DjangoObjectType):
    class Meta:
        model = TaskLabel
        fields = ("id", "name", "date_created")