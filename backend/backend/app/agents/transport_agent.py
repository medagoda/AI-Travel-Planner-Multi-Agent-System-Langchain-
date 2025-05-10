'''
import os
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file (optional)
load_dotenv()

# Set your Gemini API key
os.environ["GEMINI_API_KEY"] = "AIzaSyCKT3TbzHZt1f3w3T18vb8qBfIXSyQTcUI"

# CSV file path (use raw string or double backslashes)
csv_path = "E:\\My Travel Agent system finalize\\sri_lanka_train_schedule.csv"

# Create the agent
agent = create_csv_agent(
    ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        google_api_key="AIzaSyCKT3TbzHZt1f3w3T18vb8qBfIXSyQTcUI"  # Put your real key here or use os.getenv
    ),
    csv_path,
    verbose=True,
    allow_dangerous_code=True
)

# Prompt loop
if __name__ == "__main__":
    print("🤖 Travel Agent ready! Ask me about train times, stations, etc.")
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            response = agent.invoke(user_input)
            print("Agent:", response)
        except Exception as e:
            print("Error:", e)
'''


# app/agents/transport_agent.py

import os
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GEMINI_API_KEY = "AIzaSyCKT3TbzHZt1f3w3T18vb8qBfIXSyQTcUI"  # Replace if not using .env

class TransportAgent:
    def __init__(self):
        self.csv_path = "E:\\My Travel Agent system finalize\\sri_lanka_train_schedule.csv"
        self.agent = create_csv_agent(
            ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                temperature=0,
                google_api_key=GEMINI_API_KEY
            ),
            self.csv_path,
            verbose=True,
            allow_dangerous_code=True
        )

    def get_train_info(self, user_question: str) -> str:
        try:
            # Wrap the user question in a natural prompt
            custom_prompt = (
                "You are a helpful travel assistant. "
                "Answer in a natural and friendly tone. "
                "Here is the user's question about Sri Lankan train services:\n\n"
                f"{user_question}"
            )
            response = self.agent.invoke(custom_prompt)
            return response.get("output", response)  # extract only the text if it's in a dict
        except Exception as e:
            return f"❌ Error: {e}"



# CLI
if __name__ == "__main__":
    agent = TransportAgent()
    print("🚆 Ask me anything about Sri Lankan train schedules!")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            response = agent.get_train_info(user_input)
            print("Agent:", response)
        except Exception as e:
            print("❌ Error:", e)