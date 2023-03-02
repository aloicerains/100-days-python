import requests
import datetime as dt
import smtplib
from credentials import *
import time

MY_LAT = -1.079645
MY_LONG = 36.997860
ISS_URL = "http://api.open-notify.org/iss-now.json"


def is_close_to_iss():
    resp = requests.get(url=ISS_URL)
    resp.raise_for_status()
    data = resp.json()
    iss_position = data['iss_position']
    longitude = float(iss_position.get('longitude'))
    latitude = float(iss_position.get('latitude'))
    lat_range = (latitude - 5, latitude + 5)
    long_range = (longitude - 5, longitude + 5)
    if lat_range[0] <= MY_LAT <= lat_range[1]:
        if long_range[0] <= MY_LONG <= long_range[1]:
            return True
    return False


def send_mail():
    """Function sends mail"""
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # secure the email

        connection.starttls()
        connection.login(user=my_email, password=password)  # from credentials
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient_email,
                            msg=f"Subject: ISS Passing!\n\n{letter}")


SUN_URL = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat":-1.101822,
    "long":37.014404,
    "formatted": 0
}


def it_is_night():
    """Function determines if it's night time"""
    response = requests.get(SUN_URL, params=parameters)
    response.raise_for_status()
    data_res = response.json()
    # sunset = data['results']['sunset'].split('T')[1].split(':')[0] converted the str to time instead
    date_format = "%Y-%m-%dT%H:%M:%S+00:00"
    # conversion to time object
    sunrise = dt.datetime.strptime(data_res['results']['sunrise'], date_format)
    sunset = dt.datetime.strptime(data_res['results']['sunset'], date_format)
    # getting the time now
    time_now = dt.datetime.now()
    if time_now.hour > sunset.hour or time_now.hour < sunrise.hour:
        return True
    return False


# letter to be sent
letter = "Hey man!\n\nCome out and check the International Space Station passing by in the sky!\n\nRegards\nZac1"
while True:
    time.sleep(60)
    if it_is_night() and is_close_to_iss():
        send_mail()




