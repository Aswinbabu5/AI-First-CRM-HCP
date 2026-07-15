import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

from app.agent.tools import (
    edit_interaction,
    log_interaction,
    get_interaction,
    summarize_interaction,
    suggest_follow_up
)

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0
)

tools = [
    log_interaction,
    edit_interaction,
    get_interaction,
    summarize_interaction,
    suggest_follow_up
]

system_prompt = """
You are an AI assistant for a life-science CRM.

Your job is to help field representatives manage interactions
with healthcare professionals.

Rules:
1. Use tools whenever the user asks to log or edit CRM information.
2. Never invent an HCP or interaction ID.
3. Ask for missing required information.
4. Dates sent to tools must be in YYYY-MM-DD format.
5. Return a clear summary of the tool result.
"""

Agent_Graph = create_react_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt
)