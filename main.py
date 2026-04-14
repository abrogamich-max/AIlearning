
from os import name
from sys import prefix


user_queue = [
{"name": "Max", "request": "What is a neuroweb?", "mood": "Happy", "is_premium": True},
{"name": "ann", "request": "How to learn python or another programming language?", "mood": "Unhappy", "is_premium": False},
{"name": "Ivan", "request": "tell me a joke", "mood": "neutral", "is_premium": False}
]

def process_ai_request(user_info: dict) -> str:

    name = user_info["name"]
    query = user_info["request"]
    mood = user_info["mood"]
    is_premium = user_info["is_premium"]

    if len(query) > 25: 
        if mood == "Happy":
            greeting = f"Hello {name}! It's great to see you in a good mood!"
        elif mood == "Unhappy":
            greeting = f"Hi {name}, I'm sorry to hear you're not feeling well. How can I assist you today?"
        else:
            greeting = f"Hello {name}, how can I assist you today?"
        prefix = "[PREMIUMANSWER] " if is_premium else ""
        return f"{prefix}{greeting} You asked: '{query}'. Here's the answer to your question: [ANSWER]."
    else: 
        print(f"Processing request for {name} with a short query.")


    




print("--- Launching AI Assistant ---")

for user in user_queue:
    answer = process_ai_request(user)
    print(answer)


