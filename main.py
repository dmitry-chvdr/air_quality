import os
import logging

from dotenv import load_dotenv
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from models import LogRegModel
from prometheus.metrics import resource_usage

# Logging settings
logging.basicConfig(filename="aqi-prediction.log", level=logging.INFO)


# Get env variable
load_dotenv()
LOGREG_MODEL_PATH = os.getenv("LOGREG_MODEL_PATH")
DATA_PATH = os.getenv("DATA_PATH")

app = FastAPI()

# Service Monitoring
instrumentator = Instrumentator()
instrumentator.add(resource_usage())
instrumentator.instrument(app)
instrumentator.expose(app)

# Model
model = LogRegModel(LOGREG_MODEL_PATH, DATA_PATH)


@app.get("/predict")
async def predict(days: int):
    result = [int(value) for value in model.predict(days)]
    logging.info(f"Input days: {days}, result: {result}")
    return {"result": result}


@app.get("/fit")
async def fit(path: str):
    return {"Not implemented"}
