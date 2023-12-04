from os import read
from typing import Annotated
from fastapi import File, UploadFile
from fastapi.routing import APIRouter
from ..domain.image_classification.resnet50 import classify
import io

image_router = APIRouter()


@image_router.post("/classify", response_model=str)
def classify_image(image: UploadFile):
    return classify(image.file)
