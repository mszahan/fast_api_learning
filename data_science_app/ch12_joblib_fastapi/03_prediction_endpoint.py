import os
import contextlib
import joblib

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sklearn.pipeline import Pipeline


class PredictionInput(BaseModel):
    text: str


class PredictionOutput(BaseModel):
    category: str


class NewsgroupsModel:
    model: Pipeline | None = None
    targets: list[str] | None = None

    def load_model(self) -> None:
        """Load the model"""
        model_file = os.path.join(os.path.dirname(
            __file__), 'newsgroups_model.joblib')
        loaded_model: tuple[Pipeline, list[str]] = joblib.load(model_file)
        model, targets = loaded_model
        self.model = model
        self.targets = targets

    async def predict(self, input: PredictionInput) -> PredictionInput:
        """Runs a prediction"""
        if self.model is None or self.targets is None:
            raise RuntimeError('Model is not loaded')
        prediction = self.model.predict([input.text])
        category = self.targets[prediction[0]]
        return PredictionOutput(category=category)


newsgroups_model = NewsgroupsModel()


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    newsgroups_model.load_model()
    yield

app = FastAPI(lifespan=lifespan)


@app.post('/prediction')
async def prediction(output: PredictionInput =
                     Depends(newsgroups_model.predict)) -> PredictionOutput:
    return output
