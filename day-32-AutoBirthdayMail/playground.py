import smtplib
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
email = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_PASSWORD")

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs=email,
#         msg="Subject:Subject Goes Here\n\nContent Goes Here"
#         )

now = datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.weekday())
date_of_birth = datetime.datetime(year=2022, month=1, day=14)
print(date_of_birth)
