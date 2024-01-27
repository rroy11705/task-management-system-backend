import graphene
from core.tasks.models import Task, TaskStatus, TaskLabel
from core.tasks.types import TaskType

class TaskInput(graphene.InputObjectType):
    number = graphene.String(required=True)
    title = graphene.String(required=True)
    description = graphene.String(required=True)
    status_id = graphene.ID()
    label_ids = graphene.List(graphene.ID)
    child_of_id = graphene.ID()



class CreateTaskMutation(graphene.Mutation):
    class Arguments:
        task_details = TaskInput(required=True)

    ok = graphene.Boolean()
    task = graphene.Field(lambda: TaskType)

    @classmethod
    def mutate(cls, root, info, task_details):
        ok=True
        task_status = TaskStatus.objects.get(pk=task_details.status_id)

        task = Task(
            number=task_details.number,
            title=task_details.title,
            description=task_details.description,
            status=task_status,
            child_of=None
        )
        if task_details.child_of_id:
            task.child_of = Task.objects.get(pk=task_details.child_of_id)

        task.save()

        if task_details.label_ids:
            task_labels = TaskLabel.objects.filter(pk__in=task_details.label_ids)
            task.labels.set(task_labels)

        return CreateTaskMutation(task=task, ok=ok)
    

class UpdateTaskMutation(graphene.Mutation):
    class Arguments:
        task_details = TaskInput(required=True)

    ok = graphene.Boolean()
    task = graphene.Field(lambda: TaskType)

    @classmethod
    def mutate(cls, root, info, task_details):
        ok=True        
        task = Task.objects.get(number=task_details.number)
        task.title = task_details.title
        task.description = task_details.description
        task.status = TaskStatus.objects.get(pk=task_details.status_id)

        if task_details.child_of_id:
            task.child_of = Task.objects.get(pk=task_details.child_of_id)

        if task_details.label_ids:
            task_labels = TaskLabel.objects.filter(pk__in=task_details.label_ids)
            task.labels.set(task_labels)

        task.save()
        return CreateTaskMutation(task=task, ok=ok)
    
    
class DeleteTaskMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()
    task = graphene.Field(lambda: TaskType)

    @classmethod
    def mutate(cls, root, info, id):
        ok=True
        task = Task.objects.get(pk=id)
        task.delete()
        return DeleteTaskMutation(task=task, ok=ok)

    