from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from datasets import get_dataset_config_names, get_dataset_split_names, load_dataset, load_dataset_builder
from starlette.applications import Starlette

type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()


@query.field("hello")
def resolve_hello(*_):
    return "Hello world!"


# Create executable schema instance
schema = make_executable_schema(type_defs, query)

app = Starlette(debug=True)
app.mount("/graphql", GraphQL(schema, debug=True))