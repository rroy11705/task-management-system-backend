import graphene
from .models import Task, TaskStatus, TaskLabel
from tasks import mutations
from tasks.types import TaskType, TaskStatusType, TaskLabelType

class Query(graphene.ObjectType):

    all_tasks = graphene.List(TaskType)
    task_by_number = graphene.Field(TaskType, number=graphene.String())
    all_task_statuses = graphene.List(TaskStatusType)
    all_task_labels = graphene.List(TaskLabelType)

    def resolve_all_tasks(root, info):
        return Task.objects.all()
    
    def resolve_task_by_number(root, info, number):
        return Task.objects.get(number=number)
    
    def resolve_all_task_statuses(root, info):
        return TaskStatus.objects.all()
    
    def resolve_all_task_labels(root, info):
        return TaskLabel.objects.all()
    
class Mutation(graphene.ObjectType):
    create_task = mutations.CreateTaskMutation.Field()
    update_task = mutations.UpdateTaskMutation.Field()
    delete_task = mutations.DeleteTaskMutation.Field()
    create_task_label = mutations.CreateTaskLabelMutation.Field()
    update_task_label = mutations.UpdateTaskLabelMutation.Field()
    delete_task_label = mutations.DeleteTaskLabelMutation.Field()
    create_task_status = mutations.CreateTaskStatusMutation.Field()
    update_task_status = mutations.UpdateTaskStatusMutation.Field()
    delete_task_status = mutations.DeleteTaskStatusMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)