##################### Extra Hard Starting Project ######################
from credentials import my_email, password
import random
import datetime as dt
import smtplib
import pandas as pd


# Getting the csv data and determining if birthday is present
today = dt.datetime.now()
dataset = pd.read_csv('birthdays.csv')
birthdays = dataset.to_dict(orient='records')

# Checking the birthday
for birthday in birthdays:
    if today.month == birthday['month'] and today.day == birthday['day']:
        # Get random letter and read it
        letter_no = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_no}.txt", "r") as f:
            letter = f.read()
            letter = letter.replace("[NAME]", birthday["name"])
        # Sending the letter
        with smtplib.SMTP('smtp.gmail.com') as connection:
            # secure the email
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{birthday['email']}",
                                msg=f"Subject: Happy Birthday Wishes!\n\n{letter}")





