from fastapi import FastAPI, UploadFile
from services.disease import predict_disease
from services.llm import get_solution

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile):
    disease = predict_disease(file)
    solution = get_solution(disease)

    return {
        "disease": disease,
        "treatment": solution
    }