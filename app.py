from ariadne import ObjectType, QueryType, gql, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from datasets import get_dataset_config_names, get_dataset_split_names, load_dataset, load_dataset_builder

# Define types using Schema Definition Language (https://graphql.org/learn/schema/)
# Wrapping string in gql function provides validation and better error traceback
# type_defs = gql("""
# type Query {
#   trecs: [Trec]!
# }

# type Trec {
#     text: String
#     : Int
#     labelFine: Int
# }
# """)

type_defs = load_schema_from_path("schema.graphql")

DATASET_NAME = 'trec'

dataset = load_dataset(DATASET_NAME, split="train")

# Map resolver functions to Query fields using QueryType
query = QueryType()

# Resolvers are simple python functions
@query.field("trecs")
def resolve_trecs(*_):
    return [
        {"text": t["text"], "labelCourse": t["label-coarse"], "labelFine": t["label-fine"]}
        for t in dataset
    ] 


# Map resolver functions to custom type fields using ObjectType
trec = ObjectType("Trec")

# @person.field("fullName")
# def resolve_person_fullname(person, *_):
#     return "%s %s" % (person["firstName"], person["lastName"])

# Create executable GraphQL schema
schema = make_executable_schema(type_defs, query, trec)

# Create an ASGI app using the schema, running in debug mode
app = GraphQL(schema, debug=True)