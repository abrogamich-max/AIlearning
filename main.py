
user_data = {
"name": "Alexi",
"request": "Tell me about the quant fisics",
"mood": "Normal",
"is_premium": "True"
}

def process_ai_request(user_info):
    name = user_info["name"]
    query = user_info["request"]
    mood = user_info["mood"]
    is_premium = user_info["is_premium"]

    if mood == "Normal" and is_premium == "True":
        greeting = f"Hello, {name}. are you really Normal? "
    elif mood == "Happy" and is_premium == "True":
        grreeting = f"Hello, {name}. Im glad to hear that you are Happy! "
    else:
        greeting = f"Hello, {name}"

    print(f"--- server log: Analyse request for theme '{query}' ---")

    response = f"{greeting} I'll answer for your question about '{query}' soon."
    return response


final_answer = process_ai_request(user_data)
print(final_answer)
