from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import predict_sentiment
from dotenv import load_dotenv
import os

load_dotenv()  
API_TOKEN = os.getenv("API_TOKEN")

app = FastAPI()

class TextInput(BaseModel):
    text: str

def check_token(token: str = None):
    if token != API_TOKEN:
        raise HTTPException(401, "Неверный токен!")
    return True

@app.get("/")
def root():
    return {"message": "API работает"}

@app.get("/status")
def status(token: str = None):
    check_token(token)
    return {"status": "active", "model": "rubert-tiny"}

@app.post("/predict")
def predict(input: TextInput, token: str = None):
    check_token(token)
    
    label = predict_sentiment(input.text)  
    
    if "neg" in label:
        sentiment = "negative"
    elif "pos" in label:
        sentiment = "positive"
    else:
        sentiment = "neutral"
    
    return {
        "text": input.text,
        "sentiment": sentiment,
    }