import os
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi import FastAPI
import requests

load_dotenv()
AI_TOKEN = os.getenv("AI_TOKEN")

app = FastAPI()

class UserRequest(BaseModel):
    name: str 
    message: str

@app.get("/")
def home():
    return {"message": "Server is running", "token_loaded": bool(AI_TOKEN)}

@app.post("/ask")
def ask_ai(request: UserRequest):
    user_message = request.message

    ai_response = f"Hello, {request.name}! You asked: '{user_message}'. this is my response to your question: [ANSWER]."

    return {
        "user_sent": user_message,
        "ai_answer": ai_response
    }

