
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from tools import get_weather
import os

llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

tools = [
    Tool(
        name="Weather Tool",
        func=get_weather,
        description="Get weather of a city"
    )
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

def weather_agent(query: str):
    return agent.run(query)
