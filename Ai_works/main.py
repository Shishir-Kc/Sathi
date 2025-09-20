""" 

    This is  a Fast API Server Not A Django Server ! 


"""



from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return {
        'message':'helllo this is from Fast API'
    }