from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = 'Id of the patient in DB'), example = 'P001'):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail='Patient not found')
    
@app.get('/sort')
def sort_patients(sort_by:str = Query(...,description='sort on basis of height, weight or bmi'), order:str = Query('asc',description='sort in asc or desc order')):
    valid_fields = ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=200, detail='Invalid field, select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, description='invalid order, select asc or desc')
    sort_order = True if order=='desc' else False
    data = load_data()
    sorted_data = sorted(data.values(),key = lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data