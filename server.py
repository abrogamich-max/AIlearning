import os
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi import FastAPI
import requests
from gigachat import GigaChat

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
    try:

        with GigaChat(credentials=GIGACHAT_CREDS,
                      scope="GIGACHAT_API_PERS",
                      verify_ssl_certs=False
                      ) as giga:

            response = giga.chat(request.message)

            ai_text = response.choices[0].message.content

        return {
            "user": request.name,
            "question": request.message,
            "ai_answer": ai_text
        }
    except Exception as e:
        return {"error": str(e)}

