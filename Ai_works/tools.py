"""

        Need a tool to search for the info across web ! 

            {https://serper.dev/}

"""

from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
import os 
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()

os.environ["LANGSMITH_API_KEY"]
os.environ["LANGSMITH_WORKSPACE_ID"]
os.environ["GROQ_API_KEY"] 

# model = init_chat_model("openai/gpt-oss-120b",model_provider="groq")

@tool(description="Use the tool to search info on the web")
def search_the_web(q: str) -> dict:
    """
    Search for information across the web.

    args:
        q: query string for the info you want to search
    """
    
    return {
        "query": q,
        "result": "Here in Itahari, the current temperature is around 30°C"
    }



# # 2️⃣ User message
# user_message = [HumanMessage(content="What's the current temperature in Itahari?")]

# # 3️⃣ Bind tool to your model
# tools = [search_the_web]
# model_with_tool = model.bind_tools(tools)

# # 4️⃣ First call: model decides which tool to use
# initial_response = model_with_tool.invoke(user_message)

# # 5️⃣ Extract tool call info
# if initial_response.tool_calls:
#     tool_call = initial_response.tool_calls[0]
#     tool_args = tool_call['args']
#     tool_name = tool_call['name']

#     # Map tool name to function
#     tool_func = {"search_the_web": search_the_web}[tool_name.lower()]
    
#     # Run the tool
#     tool_result = tool_func.invoke(tool_args)
    
#     # 6️⃣ Feed the tool result back to the model
#     followup_message = [
#         HumanMessage(content="What's the current temperature in Itahari?"),
#         HumanMessage(content=f"Tool result: {tool_result}")
#     ]
    
#     final_response = model_with_tool.invoke(followup_message)
    
#     # 7️⃣ Print final model output
#     print("Final response content:", final_response.content)

# else:

#     print("No tool was called. Model output:", initial_response.content)