import os
from decouple import config
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

# --- Set up your Groq API key for LangChain ---
GROQ_API_KEY = config("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = ''

# --- Initialize the model ---
model = ChatOpenAI(model="openai/gpt-oss-20b", temperature=0, model_kwargs={"model_provider":"groq"})

# --- Define your tools ---
def search_web(query: str) -> str:
    # Replace with a real search API integration
    return f"Search results for '{query}' (mocked)."

def turn_light(on: bool) -> str:
    state = "on" if on else "off"
    return f"Turning room light {state}."

tools = [
    Tool(name="Web Search", func=search_web, description="Search the internet for information."),
    Tool(name="Turn Light On", func=lambda _: turn_light(True), description="Turns the room light on."),
    Tool(name="Turn Light Off", func=lambda _: turn_light(False), description="Turns the room light off.")
]

# --- Initialize the agent ---
agent = initialize_agent(tools, model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# --- Example usage ---
print(agent.run("Search for the latest AI news"))
print(agent.run("Turn on the room light"))
print(agent.run("Hello AI, how are you?"))
