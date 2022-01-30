import smtplib
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_SID = os.environ("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ("TWILIO_PHONE_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ("MY_PHONE_NUMBER")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("EMAIL_PROVIDER_SMTP_ADDRESS") as connection:
            connection.starttls()
            connection.login("MY_EMAIL", "MY_PASSWORD")
            for email in emails:
                connection.sendmail(
                    from_addr="MY_EMAIL",
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode(
                        'utf-8')
                )
