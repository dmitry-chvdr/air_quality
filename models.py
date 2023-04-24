import pickle
from abc import ABC, abstractmethod
from typing import Any

import pandas as pd
import requests

from methods import load_data_with_sub_index


class BaseModel(ABC):
    @abstractmethod
    def load_dataset(self, path: str) -> pd.DataFrame:
        pass

    @staticmethod
    def load_model(path: str) -> Any:
        response = requests.get(path)
        with open("model.pkl", "wb") as file:
            file.write(response.content)
        return pickle.load(open("model.pkl", "rb"))


class LogRegModel(BaseModel):
    def __init__(self, model_path: str, data_path: str):
        self.model_path = model_path
        self.model = self.load_model(model_path)
        self.data = self.load_dataset(data_path)

    def load_dataset(self, path: str) -> pd.DataFrame:
        return load_data_with_sub_index(path)

    def predict(self, days: int) -> list:
        return self.model.predict(self.data[-days:].values.tolist())
