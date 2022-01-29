import requests


class User:

    def __init__(self, attributes={}) -> None:
        self.first_name = attributes["first_name"]
        self.last_name = attributes["last_name"]
        self.email = attributes["email"]
        self.add_user_to_sheety()
        print("You're in the club!")

    def add_user_to_sheety(self):
        endpoint = "https://api.sheety.co/2441cf3e4d3f8a33fc100d25122c24f8/flightDeals/users"
        new_data = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email
            }
        }

        response = requests.post(url=endpoint, json=new_data)

        response.raise_for_status()
        print(response.text)


print("Welcome to Sufian's Flight Club")
print("We find the best flight deals and email you.")

first_name = input("What is your first name?\n")

last_name = input("What is your last name?\n")

email = input("What is your email?\n")

confirm_email = input("Enter your email again.\n")

if email == confirm_email:
    new_user = User({
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    })
else:
    print("Email mismatch. Try again.")
