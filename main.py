from fastapi import FastAPI, status
from default_respones import default_cool_responses
from router import askmodel
import random

app = FastAPI(title="callama", description="A API experiement to test or check that how user query sends to AI model and how we got our answers, in which user query or prompt travel through to an API to model, then model return response back to user back.", openapi_url="/openapi.json")

@app.get("/", status_code=status.HTTP_200_OK)
def default_respones_behaviour():
    return random.choice(default_cool_responses) 

app.include_router(askmodel.router)

