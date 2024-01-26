import graphene
from tasks.models import TaskLabel
from tasks.types import TaskLabelType


class CreateTaskLabelMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        # date_created=graphene.DateTime()

    ok = graphene.Boolean()
    task_label = graphene.Field(lambda: TaskLabelType)

    @classmethod
    def mutate(cls, root, info, name):
        ok=True
        task_label = TaskLabel(name=name)
        task_label.save()
        return CreateTaskLabelMutation(task_label=task_label, ok=ok)
    

class UpdateTaskLabelMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    ok = graphene.Boolean()
    task_label = graphene.Field(lambda: TaskLabelType)

    @classmethod
    def mutate(cls, root, info, id, name):
        ok=True
        task_label = TaskLabel.objects.get(pk=id)
        task_label.name = name
        task_label.save()
        return UpdateTaskLabelMutation(task_label=task_label, ok=ok)
    
class DeleteTaskLabelMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()
    task_label = graphene.Field(lambda: TaskLabelType)

    @classmethod
    def mutate(cls, root, info, id):
        ok=True
        task_label = TaskLabel.objects.get(pk=id)
        task_label.delete()
        return DeleteTaskLabelMutation(task_label=task_label, ok=ok)

    