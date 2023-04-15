"""
Main module
"""
import requests
from bs4 import BeautifulSoup
import smtplib
import os
my_email = 'zachaeusookello@gmail.com'
to_email = "aloiceokoth98@gmail.com"
password = os.environ.get("PASSWORD")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
              "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

def send_email(subject, url):
    """Sends emails"""
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # secure the email
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject: {subject}\n\nPlease buy it at the"
                                f"address below\n{url}")
def check_pressure_coooker_price():

    URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
    resp = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    price_tag = soup.find(name="span", class_="a-offscreen")
    price_text = price_tag.getText()
    price = float(price_text.split('$')[1])

    if price < 100:
        subj = "Pressure cooker price meets your target!"
        send_email(subject=subj, url=URL)

def check_arduino_price():
    """Checks the price of arduino sterter kit in Jumia"""
    starter_kit_url = "https://www.jumia.co.ke/generic-super-starter-kit-for-arduino-uno-r3-upgraded-version-106480531.html"
    resp = requests.get(url=starter_kit_url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    price_tag = soup.find(name="span", dir="ltr")
    price_text = price_tag.getText()
    price_str = price_text.split("KSh ")[1].split(",")
    price = float("".join(price_str))
    if price <= 5000:
        subj = "Jumia Arduino Starter Kit Price low Alert!"
        send_email(subj, starter_kit_url)

check_arduino_price()

