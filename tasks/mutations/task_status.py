import graphene
from tasks.models import TaskStatus
from tasks.types import TaskStatusType


class CreateTaskStatusMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    ok = graphene.Boolean()
    task_status = graphene.Field(lambda: TaskStatusType)

    @classmethod
    def mutate(cls, root, info, name, description):
        ok=True
        task_status = TaskStatus(name=name, description=description)
        task_status.save()
        return CreateTaskStatusMutation(task_status=task_status, ok=ok)
    

class UpdateTaskStatusMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    ok = graphene.Boolean()
    task_status = graphene.Field(lambda: TaskStatusType)

    @classmethod
    def mutate(cls, root, info, id, name, description):
        ok=True
        task_status = TaskStatus.objects.get(pk=id)
        task_status.name = name
        task_status.description = description
        task_status.save()
        return UpdateTaskStatusMutation(task_status=task_status, ok=ok)
    
class DeleteTaskStatusMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()
    task_status = graphene.Field(lambda: TaskStatusType)

    @classmethod
    def mutate(cls, root, info, id):
        ok=True
        task_status = TaskStatus.objects.get(pk=id)
        task_status.delete()
        return DeleteTaskStatusMutation(task_status=task_status, ok=ok)

    