from credentials import *
import requests
from datetime import datetime
import pytz
import os


NUTRITIONIX_URL = " https://trackapi.nutritionix.com/v2/natural/exercise"

BASIC_AUTH = os.environ.get('SHEETY_BASIC_AUTH')
APP_ID = os.getenv("NUTRIONIX_APP_ID")
API_KEY = os.getenv("NUTRIONIX_API_KEY")
query = input("Which exercise did you do? ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}
body = {
    'query': query,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}
resp = requests.post(url=NUTRITIONIX_URL, json=body, headers=headers)
resp.raise_for_status()

print(resp.json())
exercises = resp.json()['exercises']

# sheety data
my_date = datetime.now(pytz.timezone('Africa/Nairobi'))
date = my_date.date().strftime("%d/%m/%Y")
time = my_date.time().strftime("%H:%M:%S")
for exercise in exercises:
    # the keys in sheet1 will be in lowercase even if they are title case in spreadsheet
    body = {
        'sheet1': {
            "date": date,
            "time": time,
            "exercise": exercise.get('user_input'),
            "duration": exercise.get("duration_min"),
            "calories": exercise.get("nf_calories")
        }
    }
    head = {
        "Authorization": BASIC_AUTH
    }
    response = requests.post(url=SHEETY_URL, json=body, headers=head)
    response.raise_for_status()
    print(response.json())


