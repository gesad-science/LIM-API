from fastapi import FastAPI, status, Response, HTTPException
from src.treatment_entities.entities import Treatmentinput
from src.treatment_entities.treatment_center import TreatmentCenter

app = FastAPI()

@app.post('/treat/summary', tags=["Treatment"])
def get_new_answer_summary(input : Treatmentinput):
    return TreatmentCenter.run_line(line_name='summary_pipeline', input=input)

@app.post('/treat/keywords', tags=["Treatment"])
def get_new_answer_keywords(input : Treatmentinput):
    return TreatmentCenter.run_line(line_name='keywords_pipeline', input=input)

@app.post('/treat/title', tags=["Treatment"])
def get_new_answer_keywords(input : Treatmentinput):
    return TreatmentCenter.run_line(line_name='title_pipeline', input=input)
