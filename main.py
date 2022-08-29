from ariadne import (
    ObjectType,
    QueryType,
    make_executable_schema,
    load_schema_from_path,
)
from ariadne.asgi import GraphQL
from datasets import (
    get_dataset_config_names,
    get_dataset_split_names,
    load_dataset,
    load_dataset_builder,
    features,
)
from re import search, IGNORECASE


type_defs = load_schema_from_path("schema.graphql")

DATASET_NAME = "trec"

ds_builder = load_dataset_builder(DATASET_NAME)

dataset = load_dataset(DATASET_NAME)

names = {}

for k, v in ds_builder.info.features.items():
    if type(v) == features.ClassLabel:
        names[k] = v.names


query = QueryType()


@query.field("questions")
def resolve_trecs(*_, split=None, text=None, skip=None, first=None):
    splits = get_dataset_split_names(DATASET_NAME)
    if split:
        splits = [split]
    
    output = []
    for s in splits:
        output = [
                {
                    "split": s,
                    "text": q["text"],
                    "labelCourse": q["label-coarse"],
                    "labelFine": q["label-fine"],
                }
                for q in dataset[s]
            ]

    if text:
        output = filter(lambda t: search(text, t["text"], IGNORECASE), output)

    if skip:
        output = output[skip:]

    if first:
        output = output[:first]

    return output


question = ObjectType("Question")


@question.field("labelCourseName")
def resolve_label_course_name(question, *_):
    return names["label-coarse"][question["labelCourse"]]


@question.field("labelFineName")
def resolve_label_fine_name(question, *_):
    return names["label-fine"][question["labelFine"]]


@question.field("label")
def resolve_label(question, *_):
    return f"{names['label-coarse'][question['labelCourse']]}:{names['label-fine'][question['labelFine']]}"


schema = make_executable_schema(type_defs, query, question)

app = GraphQL(schema, debug=True)
