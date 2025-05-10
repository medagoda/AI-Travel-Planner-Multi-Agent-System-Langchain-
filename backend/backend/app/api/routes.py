
from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.weather_agent import WeatherChatAgent
from app.agents.attractions_agent import AttractionsAgent
from app.agents.transport_agent import TransportAgent
from app.utils.intent_classifier import IntentClassifier  # Save it as a new file

import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

# Initialize agents
weather_agent = WeatherChatAgent()
transport_agent = TransportAgent()
attractions_agent = AttractionsAgent()
intent_classifier = IntentClassifier(api_key=os.getenv("GEMINI_API_KEY"))

class QueryModel(BaseModel):
    message: str

@router.post("/ask")
def ask_agent(query: QueryModel):
    intent = intent_classifier.classify(query.message)

    if intent == "weather":
        return {"agent": "weather", "response": weather_agent.ask(query.message)}
    elif intent == "transport":
        return {"agent": "transport", "response": transport_agent.get_train_info(query.message)}
    elif intent == "attraction":
        return {"agent": "attraction", "response": attractions_agent.get_response(query.message)}
    else:
        return {"agent": "none", "response": "❌ Sorry, I couldn't understand your request. Please ask about weather, transport, or attractions."}



