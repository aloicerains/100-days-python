from credentials import *
import requests
from twilio.rest import Client
import os

# Getting data from openweather
open_weather_url = "https://api.openweathermap.org/data/3.0/onecall"
parameters = {
    "lat": lat,
    "lon": long,
    "exclude": "current,daily",
    "appid": os.environ.get('API_KEY')
}
resp = requests.get(url=open_weather_url, params=parameters)
resp.raise_for_status()
weather_data = resp.json()

# connecting to twilio

it_will_rain = False
for weather in weather_data['hourly'][:12]:
    for condition in weather['weather']:
        if int(condition['id']) < 700:
            it_will_rain = True
if it_will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, bring an ☂️",
        from_=source_phone_no,
        to=to_phone_no
    )
    print(message.status)
else:
    print('No rains today')

