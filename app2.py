from ariadne import QueryType, make_executable_schema, load_schema_from_path, ObjectType
from ariadne.asgi import GraphQL
from datasets import get_dataset_config_names, get_dataset_split_names, load_dataset, load_dataset_builder
from starlette.applications import Starlette

# type_defs = load_schema_from_path("schema.graphql")


type_defs = """
type Query {
  trecs: [Trec]!
}

type Trec {
    text: String
    labeCourse: Int
    labeFine: Int
}
"""



query = QueryType()

ds = []
for i in range(0,5):
    ds.append({'label-coarse': i*10, 'label-fine': i, 'text':f"f{i}"})

trec = ObjectType("Trec")
# @trec.field("text")
def resolve_value(*_, value=None):
    return value


@query.field("trecs")
def resolve_trecs(*_):
    output = []
    for t in ds:
        # obj_t = ObjectType("Trec")
        trec.set_field("text",resolve_value(value=t['text']))
        trec.set_field("labeCourse",resolve_value(value=t['label-coarse']))
        trec.set_field("labeFine",resolve_value(value=t['label-fine']))
        output.append(trec)
    return output



# Create executable schema instance
schema = make_executable_schema(type_defs, query, trec)

app = Starlette(debug=True)
app.mount("/graphql", GraphQL(schema, debug=True))