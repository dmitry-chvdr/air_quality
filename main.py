import os

from dotenv import load_dotenv
from fastapi import FastAPI

from models import LogRegModel

load_dotenv()

LOGREG_MODEL_PATH = os.getenv("LOGREG_MODEL_PATH")
DATA_PATH = os.getenv("DATA_PATH")

app = FastAPI()

model = LogRegModel(LOGREG_MODEL_PATH, DATA_PATH)


@app.get("/predict")
async def predict(days: int):
    return {"result": [int(value) for value in model.predict(days)]}
