import requests
from datetime import datetime
from decouple import config

EXERCISE_ENDPOINT = config("EXERCISE_ENDPOINT")
SHEETY_ENDPOINT = config("SHEETY_ENDPOINT")

APP_ID = config("APP_ID")
API_KEY = config("API_KEY")
TOKEN = config("TOKEN")

user_input = input("Tell me which exercises you did: ")

today = datetime.now()
formatted_date = today.strftime("%m/%d/%Y")
formatted_time = today.strftime("%X")

exercise_params = {
 "query": user_input,
 "gender": "male",
 "weight_kg": 82,
 "height_cm": 187,
 "age": 18
}

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_response = requests.post(EXERCISE_ENDPOINT, json=exercise_params, headers=exercise_headers)
data = exercise_response.json()["exercises"][0]
exercise = data["user_input"].title()
duration = data["duration_min"]
calories = data["nf_calories"]

sheets_params = {
    "workout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheets_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

sheets_response = requests.post(SHEETY_ENDPOINT, json=sheets_params, headers=sheets_headers)
print(sheets_response.status_code)