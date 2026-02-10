import os
from dotenv import load_dotenv
from langchain.agents import create_react_agent
from langchain.agents.agent import AgentExecutor
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from tools import get_current_weather, get_weather_forecast, get_flights, get_hotels

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    temperature=0.4,
    openai_api_key=os.getenv("GROQ_API_KEY"),
    openai_api_base="https://api.groq.com/openai/v1"
)

tools = [
    Tool(name="Current Weather", func=get_current_weather, description="Get weather"),
    Tool(name="Weather Forecast", func=get_weather_forecast, description="Get forecast"),
    Tool(name="Flights", func=get_flights, description="Get flights"),
    Tool(name="Hotels", func=get_hotels, description="Get hotels"),
]

prompt = PromptTemplate.from_template("""
You are a travel assistant.

Use the following tools:

{tools}

Available tool names:
{tool_names}

Use this format:

Question: {input}
Thought: you should always think about what to do
Action: the action to take (must be one of {tool_names})
Action Input: the input to the action
Observation: the result
... (repeat if needed)
Final Answer: the final response to the user

Begin!

Question: {input}
Thought:{agent_scratchpad}
""")

agent = create_react_agent(llm, tools, prompt)

travel_agent = AgentExecutor(
         agent=agent, 
        tools=tools, 
        verbose=True,
        handle_parsing_errors=True)