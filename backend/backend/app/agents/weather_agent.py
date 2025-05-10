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





'''

# API_KEY = "a9520c42713b0ad585a9fa95fd7b260c"

import os
import requests
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.agent_types import AgentType

# Load your environment variables
load_dotenv()

# Set your OpenWeatherMap API key and Gemini API key (must be set in .env)
#WEATHER_API_KEY = os.getenv("a9520c42713b0ad585a9fa95fd7b260c")
# GEMINI_API_KEY = os.getenv("AIzaSyC-Z9UGQRqk4UCjoXBvdt678WRBLhu_c6g")

WEATHER_API_KEY = "a9520c42713b0ad585a9fa95fd7b260c"
GEMINI_API_KEY = "AIzaSyC-Z9UGQRqk4UCjoXBvdt678WRBLhu_c6g"

# Weather fetch function
def get_weather(city="Colombo", country="LK"):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city},{country}",
        "appid": WEATHER_API_KEY,
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

# Tool wrapper so LangChain agent can use it
def weather_tool(city: str) -> str:
    return get_weather(city)

# Define the tool for LangChain
weather_tool_obj = Tool(
    name="GetWeather",
    func=weather_tool,
    description="Returns the current weather in a given Sri Lankan city. Input should be the city name only."
)

# Initialize the LLM (Gemini 2.0 Flash via LangChain)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2,
    google_api_key=GEMINI_API_KEY
)

# Create an agent with the tool
agent = initialize_agent(
    tools=[weather_tool_obj],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Main loop
if __name__ == "__main__":
    print("🌦️ Ask about weather in Sri Lankan cities (e.g., 'What’s the weather like in Kandy?')")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = agent.run(query)
        print(f"\n🤖: {response}\n")


'''


import os
import requests
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.agent_types import AgentType
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser




WEATHER_API_KEY = "a9520c42713b0ad585a9fa95fd7b260c"
GEMINI_API_KEY =  "AIzaSyC-Z9UGQRqk4UCjoXBvdt678WRBLhu_c6g"



class WeatherChatAgent:
    def __init__(self):
        load_dotenv()

        self.weather_tool_obj = Tool(
            name="GetWeather",
            func=self.weather_tool,
            description="Returns the current weather in a given Sri Lankan city. Input should be the city name only."
        )

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.2,
            google_api_key=GEMINI_API_KEY
        )

        self.agent = initialize_agent(
            tools=[self.weather_tool_obj],
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )

    def get_weather(self, city="Colombo", country="LK"):
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": f"{city},{country}",
            "appid": WEATHER_API_KEY,
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

    def weather_tool(self, city: str) -> str:
        return self.get_weather(city)

    def ask(self, query: str) -> str:
        return self.agent.invoke(query)

# Usage (for CLI testing or plug into your API backend)
if __name__ == "__main__":
    agent = WeatherChatAgent()
    print("🌦️ Ask about weather in Sri Lankan cities (e.g., 'What’s the weather like in Kandy?')")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = agent.ask(query)
        print(f"\n🤖: {response}\n")
