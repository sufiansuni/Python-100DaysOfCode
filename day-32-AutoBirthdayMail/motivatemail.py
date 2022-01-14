import smtplib
from dotenv import load_dotenv
import os
import datetime
import random

load_dotenv()
email = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_PASSWORD")


if datetime.datetime.now().weekday() == 4:
    with open("day-32-AutoBirthdayMail\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Motivational Quote of The Day\n\n{quote}"
        )
