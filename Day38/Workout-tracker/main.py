import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = "74"
HEIGHT_CM = "180.34"
AGE = "21"
USERNAME = "Your USERNAME"
PASSWORD = "Your PASSWORD"

APP_ID = "ef7c2688"
API_KEY = "e1327264f55f439f36624c43a2bd94fc"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/b7c5682fd148fd0795ae64da8e01091c/workoutTracker/workouts"

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

################### Start of Step 4 Solution ######################

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)



# Basic Authentication
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(USERNAME,PASSWORD))
print(sheet_response)