from langchain.chat_models import init_chat_model
import os 
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from tools import search_the_web

load_dotenv()

os.environ["LANGSMITH_API_KEY"]
os.environ["LANGSMITH_WORKSPACE_ID"]
os.environ["GROQ_API_KEY"] 

model = init_chat_model("openai/gpt-oss-120b",model_provider="groq")

prompt_template = ChatPromptTemplate([
  ('system','You are an ai named SKY made by Kc.tech '),
  MessagesPlaceholder("msg")
])



async def generate_text(prompt):
  up_prompt = prompt_template.invoke({
    "msg":[HumanMessage(content=prompt)]
  })
  # user_message  = model.invoke(up_prompt)
  
  tools =[search_the_web]
  model_with_tools = model.bind_tools(tools)
  initial_response = model_with_tools.invoke(up_prompt)
  if initial_response.tool_calls:
    tool_call = initial_response.tool_calls[0]
    tool_args = tool_call['args']
    tool_name = tool_call['name']

    tool_func = {"search_the_web": search_the_web}[tool_name.lower()]
    tool_result = tool_func.invoke(tool_args)

    followup_message = [
        HumanMessage(content=prompt),
        HumanMessage(content=f"Tool result: {tool_result}")
    ]
  
    final_response = model_with_tools.invoke(followup_message)
    return final_response.content
  else:
    return initial_response.content
  
  


