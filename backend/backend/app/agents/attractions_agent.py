'''
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_google_genai import ChatGoogleGenerativeAI

# Step 1: Initialize the LLM (Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key="AIzaSyCKT3TbzHZt1f3w3T18vb8qBfIXSyQTcUI"
)

# Step 2: Create a prompt template
custom_prompt = PromptTemplate(
    input_variables=["input"],
    template="""
You are a helpful and smart assistant who uses Wikipedia to answer user questions.
Answer concisely and clearly.

User's Question: {input}
""".strip()
)

# Step 3: Wrap it with LLMChain
llm_chain = LLMChain(
    llm=llm,
    prompt=custom_prompt
)

# Step 4: Initialize Wikipedia Tool
wikipedia_api_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="WikipediaQueryRun",
    func=WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper).run,
    description="Use this tool to query Wikipedia and fetch relevant information."
)

# Step 5: Create the agent with the custom prompt
agent = initialize_agent(
    tools=[wikipedia_tool],
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Step 6: Run a question

if __name__ == "__main__":
    print("🤖 Travel Agent ready! Ask me about places, etc.")
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



from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_google_genai import ChatGoogleGenerativeAI


class AttractionsAgent:
    def __init__(self, api_key: str):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            google_api_key=api_key
        )

        self.prompt = PromptTemplate(
            input_variables=["input"],
            template="""
You are a helpful and smart assistant who uses Wikipedia to answer user questions.
Answer concisely and clearly.

User's Question: {input}
""".strip()
        )

        self.wikipedia_tool = Tool(
            name="WikipediaQueryRun",
            func=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()).run,
            description="Use this tool to query Wikipedia and fetch relevant information."
        )

        self.agent = initialize_agent(
            tools=[self.wikipedia_tool],
            llm=self.llm,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False,
             handle_parsing_errors=True
        )

    def get_response(self, question: str) -> str:
        try:
            return self.agent.invoke(question)
        except Exception as e:
            return f"Error: {str(e)}"


# Test from CLI
if __name__ == "__main__":
    api_key = "AIzaSyCKT3TbzHZt1f3w3T18vb8qBfIXSyQTcUI"
    agent = AttractionsAgent(api_key)

    print("🗺️ Attractions Agent Ready. Ask about tourist places or say 'exit'.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent.get_response(user_input)
        print("Agent:", response)