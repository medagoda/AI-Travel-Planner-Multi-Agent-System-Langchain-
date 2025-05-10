"""
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Sri Lanka Agent API",
    description="Interact with LLM agents for weather and transport info",
    version="1.0"
)

app.include_router(router)


"""
import email_validator

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
