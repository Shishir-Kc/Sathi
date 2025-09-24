""" 

    This is  a Fast API Server Not A Django Server ! 

    
    Ai related Task will be done here ! 

"""
from fastapi import FastAPI,Depends
from Generate_text import generate_text
from pydantic import BaseModel
from BUCKET import upload_to_bucket
from Authentication import verify_jwt
import base64

"""
    preparing for expected json data

"""
class Chat(BaseModel):
    prompt:str

class Image_Upload(BaseModel):
    filename:str
    file_content:str
    file_type:str


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
async def Chat(data: Chat,user=Depends(verify_jwt)):
    response = await generate_text(data.prompt)
    return {
        'response':response
    }

@app.post('/upload/')
async def Upload_image(data:Image_Upload,user=Depends(verify_jwt)):
    print("payload Recived")
    file_name =data.filename
    file_bytes = base64.b64decode(data.file_content)
    response = await upload_to_bucket(bucket_name ="images",file_name = file_name,file_bytes = file_bytes,file_type=data.file_type)
    
    return response
