from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import math

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()

ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
# proxy_client = TwilioHttpClient(
#     proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

client = Client(account_sid, auth_token)
# client = Client(account_sid, auth_token, http_client=proxy_client)

TWILIO_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']
MY_PHONE_NUMBER = os.environ['MY_PHONE_NUMBER']


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_api_params = {
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_api_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

stock_data_list = list(stock_data.values())

yesterday_closing = float(stock_data_list[0]["4. close"])
# print(yesterday_closing)

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing = float(stock_data_list[1]["4. close"])
# print(day_before_yesterday_closing)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
raw_diff = yesterday_closing - day_before_yesterday_closing
positive_diff = abs(raw_diff)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = positive_diff/day_before_yesterday_closing * 100
# print(percent_diff)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_diff > 5:
    # print("Get News")

    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_api_params = {
        "q": COMPANY_NAME,
        "sortBy": "popularity",
        "apikey": NEWS_API_KEY
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_api_params)
    news_response.raise_for_status()

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    news_data = news_response.json()["articles"][:3]

# print(news_data)

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [{"title": article["title"],
                           "description": article["description"]} for article in news_data]
# print(formatted_articles)

# TODO 9. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        if raw_diff > 0:
            change_symbol = "🔺"
        else:
            change_symbol = "🔻"

        headline = article["title"]
        brief = article["description"]

        body = f"\nTSLA: {change_symbol}{math.floor(percent_diff)}%\n"\
            f"Headline: {headline}\n"\
            f"Brief: {brief}"

        # print(body)

        message = client.messages \
            .create(
                body=body,
                from_=TWILIO_PHONE_NUMBER,
                to=MY_PHONE_NUMBER
            )
        print("SMS Sent. Message SID: ", message.sid)

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.

or

TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
