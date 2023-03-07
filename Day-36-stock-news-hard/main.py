import requests
from twilio.rest import Client
import os
from credentials import *

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


# obtain the news
def get_news(perc: float):
    """Fetches the latest news about the company"""
    parameters = {
        "q": COMPANY_NAME,
        "language": "en",
        "apiKey": os.environ.get("NEWS_API_KEY")
    }

    resp = requests.get(url=NEWS_ENDPOINT, params=parameters)
    resp.raise_for_status()
    articles_data = resp.json()['articles'][:3]
    send_message(articles_data, perc)


def send_message(articles: list, perc: float):
    """Sends message to the user"""
    for article in articles:
        client = Client(account_sid, auth_token)
        if perc > 0:
            message = client.messages.create(
                body=f"{STOCK}: 🔺 {perc} %\nHeadline: {article.get('title')}\nBrief: {article.get('description')}",
                from_=source_phone_no,
                to=to_phone_no
            )
        else:
            message = client.messages.create(
                body=f"{STOCK}: 🔻 {perc} %\nHeadline: {article.get('title')}\nBrief: {article.get('description')}",
                from_=source_phone_no,
                to=to_phone_no
            )


# Obtain Tesla stock prices
params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "60min",
    "outputsize": "compact",
    "apikey": os.environ.get("STOCK_TRADING_API_KEY")
}


response = requests.get(url=STOCK_ENDPOINT, params=params)
data = response.json()['Time Series (Daily)']
data_list = [value for key, value in data.items()]

# check data for consecutive days given data are arranged from yesterday backwards
before_yesterday_close = float(data_list[1]['4. close'])
yesterday_close = float(data_list[0]['4. close'])
difference = yesterday_close - before_yesterday_close
percent = round(difference/yesterday_close * 100)
if abs(percent) > 5:
    get_news(percent)

