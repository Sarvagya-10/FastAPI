from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as fr:
        data = json.load(fr)
    return data

@app.get("/")
def root():
    return {'message': 'Hello world'}

@app.get("/name")
def get_name():
    return {'name': 'Sarvagya'}

@app.get("/view")
def view():
    data = load_data()
    return data
