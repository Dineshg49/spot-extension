from enum import Enum
from typing import Final, List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# from handlers import spot_handler
from handlers.spot_handler import SpotHandler

spot_handler = SpotHandler()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InsightType(str ,Enum):
    MISSPELLED_WORD: Final = "MISSPELLED_WORD"
    BAD_GRAMMAR: Final = "BAD_GRAMMAR"
    SEXIST_WORD: Final = "SEXIST_WORD"
    SEXIST_PHRASE: Final = "SEXIST_PHRASE"

class SpotInsight(BaseModel):
    type: InsightType
    suggestion: List[str]

class SpotResponse(BaseModel):
    loc_start: int
    loc_end: int
    message: SpotInsight

# Don't do this in production!

@app.post("/v1/spot/process")
async def create_user(text: str) -> str:
    response = spot_handler.process(text)
    return response

@app.get("/v1/spot/process/get-sample-data")
async def get_user() -> str:
    response = "This is the text returned by the user"
    return response


# server.py [Will only handle request / response No business logic]
# cli.py 
# handlers/spot_handler.py [No HTTP related verbs here]
# ml_models/... [Only ML related code]
# ---- process