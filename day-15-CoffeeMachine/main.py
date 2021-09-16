MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

ingredients = ["water", "milk", "coffee"]


def check_ingredients(drink):
    for i in ingredients:
        if MENU[drink]["ingredients"][i] > resources[i]:
            return "Sorry there is not enough " + i + "."
    return "ok"


def process_ingredients(drink):
    for i in ingredients:
        resources[i] -= MENU[drink]["ingredients"][i]
    print("Here is your " + drink + ". Enjoy!")


def check_transaction(drink):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickels?: "))
    pennies = int(input("How many Pennies?: "))

    user_money = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    print("You have inserted $%.2f" % user_money)
    if MENU[drink]["cost"] > user_money:
        return "​Sorry that's not enough money. Money refunded.​"
    else:
        resources["money"] += MENU[drink]["cost"]
        change = user_money - MENU[drink]["cost"]
        return "%.2f" % change


machine_on = True

while machine_on:
    request = input("​What would you like? (espresso/latte/cappuccino):")
    if request == "off":
        machine_on = False
    if request == "report":
        print("Water: ", resources["water"], "ml")
        print("Milk: ", resources["milk"], "ml")
        print("Coffee: ", resources["coffee"], "g")
        print("Money: $", "%.2f" % resources["money"])
    if request == "espresso" or request == "latte" or request == "cappuccino":
        check = check_ingredients(request)
        if check != "ok":
            print(check)
        else:
            transaction = check_transaction(request)
            if transaction == "​Sorry that's not enough money. Money refunded.​":
                print(transaction)
            else:
                if transaction != "0.00":
                    print("Here is $", transaction, "dollars in change.")
                process_ingredients(request)
