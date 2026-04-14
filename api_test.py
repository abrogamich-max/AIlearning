import requests

def get_space_data():
    url = "http://api.open-notify.org/astros.json"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
        return None


space_info = get_space_data()

if isinstance(space_info, dict):
    number = space_info["number"]
    print(f"Interesting fact for our AI: There are {number} people in space right now.")


    print("List of an austronauts")
    for person in space_info["people"]:
        print(f"- {person['name']} on the {person['craft']}")
else:
    print(space_info)