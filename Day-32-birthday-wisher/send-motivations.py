import smtplib
from credentials import my_email, password
import datetime as dt
import random



# check day and time
day = dt.datetime.now()
if day.weekday() == 1:
    # opening the quotes file
    quotes = []
    with open('quotes.txt', 'r') as file:
        for line in file:
            quotes.append(line.strip())
    quot_of_day = random.choice(quotes)

    if day.hour == 8:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            # secure the email
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='zacchaeusokoth4@gmail.com',
                                msg=f"Subject: Tuesday Motivations\n\n{quot_of_day}")

# working with datetime
# today = dt.datetime.now()
# hour = today.hour
# minute = today.minute
# week_day = today.weekday()
#print(week_day)

# creating a time of your choosing
#birth_day = dt.datetime(year=1995, month=11, day=4, hour=10)
#print(birth_day)