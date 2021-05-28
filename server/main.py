from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    tom = "tom"
    jack = "jack"
    asia = "asia"


app = FastAPI()


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.tom:
        return {"success": True, "model_name": model_name, "message": "Tom test"}

    if model_name == ModelName.asia:
        return {"success": True, "model_name": model_name, "message": "Asia test"}

    return {"success": True, "model_name": model_name, "message": "Unknown test"}
