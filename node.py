from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm, tools

load_dotenv()

system_message = """
You are a helpful assistant that that can use tools to answer questions
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """A simple agent that uses the tools to answer questions."""
    response = llm.invoke([{"role": "system", "content": system_message}, *state["messages"]])
    return {"messages": [response]}

tool_node = ToolNode(tools=tools)