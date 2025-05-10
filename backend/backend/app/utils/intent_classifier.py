from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


api_key = "AIzaSyC-Z9UGQRqk4UCjoXBvdt678WRBLhu_c6g"


class IntentClassifier:
    def __init__(self, api_key: str):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            google_api_key=api_key
        )

        self.prompt = PromptTemplate(
            input_variables=["query"],
            template="""
You are an intent classification assistant.
Given the user's query, classify it into one of the following categories:

- weather
- transport
- attraction

If it doesn't match any category, respond with "unknown".

User query: {query}
Category:
""".strip()
        )

        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def classify(self, query: str) -> str:
        try:
            response = self.chain.run(query).strip().lower()
            return response if response in ["weather", "transport", "attraction"] else "unknown"
        except Exception as e:
            return "unknown"
