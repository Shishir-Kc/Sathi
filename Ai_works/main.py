""" 

    This is  a Fast API Server Not A Django Server ! 

    
    Ai related Task will be done here ! 

"""
from click import prompt
from fastapi import FastAPI
from Generate_text import Generate_text
from pydantic import BaseModel
"""
    preparing for expected json data

"""
class Chat(BaseModel):
    prompt:str

app = FastAPI()




"""
    General API testing ! 

"""



@app.get("/hello")
async def hello():
    return {
        'message':'helllo this is from Fast API'
    }

"""

    APi Routing for Ai Response ! 

"""
@app.post('/chat/')
async def Chat(data: Chat):
    response = await Generate_text(data.prompt)
    return {
        'response':response
    }
