from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return{'message':'Hello world'}

@app.get("/name")
def hello():
    return{'name':'Sarvagya'}
