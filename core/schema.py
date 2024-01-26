import graphene

import tasks.schema as tasks
import users.schema as users

class Query(tasks.schema.Query, users.schema.Query, graphene.ObjectType):
    # Inherits all classes and methods from app-specific queries, so no need
    # to include additional code here.
    pass

class Mutation(tasks.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    # Inherits all classes and methods from app-specific mutations, so no need
    # to include additional code here.
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)