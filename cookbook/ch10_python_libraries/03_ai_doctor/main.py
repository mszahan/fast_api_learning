from typing import Annotated
from pydantic import create_model
from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager

import joblib
from huggingface_hub import hf_hub_download

from utils import symptoms_list


ml_model = {}
REPO_ID = "AWeirdDev/human-disease-prediction"
FILENAME = "sklearn_model.joblib"


@asynccontextmanager
async def lifespan(app: FastAPI):
    ml_model['doctor'] = joblib.load(
        hf_hub_download(
            repo_id=REPO_ID,
            filename=FILENAME,
        )

    )
    yield
    ml_model.clear()

app = FastAPI(title='AI doctor', lifespan=lifespan)


query_parameters = {
    symp: (bool, False)
    for symp in symptoms_list[:10]
}


Symptoms = create_model(
    'Symptoms', **query_parameters

)


@app.get('/diagnosis')
async def get_diagnosis(symptoms: Annotated[type, Depends(Symptoms)]):
    array = [int(value) for _, value in symptoms.model_dump().items()]
    array.extend([0] * (len(symptoms_list) - len(array)))
    len(symptoms_list)
    diseases = ml_model['doctor'].predict([array])
    return {
        'diseases': [disease for disease in diseases]
    }
