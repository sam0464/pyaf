
from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import weather_agent


app = FastAPI(title="SanchAI Weather Assistant")

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(query: Query):
    response = weather_agent(query.message)
    return {"response": response}
