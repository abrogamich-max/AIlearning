from fastapi import FastAPI
import requests

app = FastAPI()

def get_space_data():
    url = "http://api.open-notify.org/astros.json"
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    except Exception:
        return{"error": "Failed to fetch space data"}



@app.get("/")
def home():
    return{"message": "Its a backend of our AI assistant"}

@app.get("/status")
def get_status():
    space_info = get_space_data()
    return {
        "space_info": space_info
    }

@app.get("/ai-status")
def ai_status():
    return {
        "model": "GigaChat", "status": "learning", "step": 5
    }