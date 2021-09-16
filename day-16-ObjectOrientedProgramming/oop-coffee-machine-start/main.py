from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

print(coffee_maker.resources)

while machine_on:
    request = input(f"What would you like? {Menu.get_items(menu)}:")
    if request == "off":
        machine_on = False
    elif request == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(request)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
