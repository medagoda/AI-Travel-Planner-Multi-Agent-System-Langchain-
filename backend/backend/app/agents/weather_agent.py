"""
import os
import requests
from dotenv import load_dotenv


# Load API key from .env
load_dotenv()
# API_KEY = os.getenv("WEATHER_API_KEY")

API_KEY = "a9520c42713b0ad585a9fa95fd7b260c"

def get_weather(city="Colombo", country="LK"):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city},{country}",
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            return (f"🌤️ Weather in {city}:\n"
                    f"Condition: {weather}\n"
                    f"Temperature: {temp}°C (Feels like {feels_like}°C)\n"
                    f"Humidity: {humidity}%")
        else:
            return f"❌ Error: {data['message']}"
    except Exception as e:
        return f"❌ Failed to get weather: {e}"

# Example usage
if __name__ == "__main__":
    city = input("Enter Sri Lankan city: ")
    print(get_weather(city))

    

"""


import os
import requests
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load environment variables
load_dotenv()
# API_KEY = os.getenv("WEATHER_API_KEY")
API_KEY = "a9520c42713b0ad585a9fa95fd7b260c"

# Define weather fetching function
def get_weather(city="Colombo", country="LK"):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city},{country}",
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            return (f"🌤️ Weather in {city}:\n"
                    f"Condition: {weather}\n"
                    f"Temperature: {temp}°C (Feels like {feels_like}°C)\n"
                    f"Humidity: {humidity}%")
        else:
            return f"❌ Error: {data['message']}"
    except Exception as e:
        return f"❌ Failed to get weather: {e}"

# LangChain tool
tools = [
    Tool(
        name="WeatherTool",
        func=get_weather,
        description="Fetches the current weather for a city in Sri Lanka."
    ),
]

# Prompt template
weather_prompt = PromptTemplate(
    input_variables=["city", "country"],
    template="You are a helpful assistant. Please provide the current weather information for {city}, {country}. Respond in a friendly and clear format."
)

# Load HuggingFace model and tokenizer
model_id = "tiiuae/falcon-7b-instruct"  # You can change this to any other model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

# Create pipeline for LangChain
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_new_tokens=256)
hf_llm = HuggingFacePipeline(pipeline=pipe)

# Initialize the agent
agent = initialize_agent(
    tools,
    llm=hf_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Main user interaction
if __name__ == "__main__":
    user_input = input("Ask a question (e.g., weather in Colombo): ")
    response = agent.run(user_input)
    print(response)
