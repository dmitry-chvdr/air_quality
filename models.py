import pickle
from abc import ABC, abstractmethod

from methods import load_data_with_sub_index


class BaseModel(ABC):

    @abstractmethod
    def load_dataset(self, *args, **kwargs):
        pass

    @abstractmethod
    def predict(self, *args, **kwargs):
        pass


class LogRegModel(BaseModel):
    def __init__(self, model_path: str, data_path: str):
        self.model = pickle.load(open(model_path, "rb"))
        self.data = self.load_dataset(data_path)

    def load_dataset(self, path):
        return load_data_with_sub_index(path)

    def predict(self, days: int) -> list:
        return self.model.predict(self.data[-days:].values.tolist())