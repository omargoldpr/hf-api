from msilib.schema import Class
import typing
import strawberry

from datasets import get_dataset_config_names, get_dataset_split_names, load_dataset, load_dataset_builder
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
Class 