from msilib.schema import Class
import typing
import strawberry

from datasets import get_dataset_config_names, get_dataset_split_names, load_dataset, load_dataset_builder
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.tools import create_type

DATASET_NAME = 'trec'

ds_builder = load_dataset_builder(DATASET_NAME)

@strawberry.field
def hello(info) -> str:
    return "World"


def get_name(info) -> str:
    return info.context.user.name
 
my_name = strawberry.field(name="myName", resolver=get_name)


Query = create_type("Query", [hello, my_name])


schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")