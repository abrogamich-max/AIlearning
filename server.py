import os
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi import FastAPI
import requests
from gigachat import GigaChat

from database import init_db, save_message, get_history

init_db()

load_dotenv()
GIGACHAT_CREDS = os.getenv("GIGACHAT_CREDENTIALS")

if not GIGACHAT_CREDS:
    print("❌ ОШИБКА: Ключ GIGACHAT_CREDENTIALS не найден в .env!")
else:
    print(f"✅ Ключ загружен успешно (длина: {len(GIGACHAT_CREDS)} символов)")

app = FastAPI()

class UserRequest(BaseModel):
    name: str 
    message: str

@app.get("/")
def home():
    return {"message": "AI Backend is LIVE", "ai_provider": "GigaChat"}

@app.post("/ask")
def ask_ai(request: UserRequest):

    history = get_history(request.name)

    context = "Its a history of massages:\n"
    for user_msg, ai_msg in reversed(history):
        context += f"user: {user_msg}\nAI: {ai_msg}\n"

    full_prompt = f"{context}\nNewQuestion from {request.name}: {request.message}"



    try:

        with GigaChat(credentials=GIGACHAT_CREDS,
                      scope="GIGACHAT_API_PERS",
                      verify_ssl_certs=False
                      ) as giga:

            response = giga.chat(full_prompt)

            ai_text = response.choices[0].message.content

        save_message(request.name, request.message, ai_text)

        return {
            "ai_answer": ai_text, 
            "memory_status": f"В базе сохранено сообщений для {request.name}: {len(history)+ 1}"
        }
    except Exception as e:
        return {"error": str(e)}

