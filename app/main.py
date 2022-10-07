from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.router import rating
from app.db.database import engine, Base

app = FastAPI(
    title="TranslationRatingApp",
    description="Translation Rating Api",
    version="0.0.1",
)

app.include_router(rating.router)


@app.on_event("startup")
def app_startup():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@app.get("/ping", tags=['health'])
def ping():
    return "pong"