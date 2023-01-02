import requests
from datetime import datetime


APP_ID = "bb37d633"
API_KEY = "f7915f016e2cc0e2e25bfea43c7b1bda	"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Tell me which exercises you did: ")
GENDER = "female"
WEIGHT = 43
HEIGHT = 161
AGE = 25

nutritionix_params = {
        "query": exercise,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=headers)
result = response.json()
print(result)

sheety_endpoint = "https://api.sheety.co/b672c2a6f4921443dbe093c3953147d4/myWorkouts/workouts"

today = datetime.now()
# print(today.strftime("%d/%m/%Y"))

for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today.strftime('%d/%m/%Y'),
            "time": today.strftime('%H:%M:%S'),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheety_inputs)

    print(sheet_response.text)

