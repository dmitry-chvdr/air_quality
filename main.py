from fastapi import FastAPI

from models import LogRegModel

MODEL_PATH = "./models/LOGREG.pkl"
DATA_PATH = "https://raw.githubusercontent.com/dmitry-chvdr/aqi_prediction/master/ts_air_quality_index_2013_2020.csv"

app = FastAPI()

model = LogRegModel(MODEL_PATH, DATA_PATH)


@app.get("/predict")
async def predict(days: int):
    return {"result": [int(value) for value in model.predict(days)]}
