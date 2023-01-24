from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = Menu()
coffee = CoffeeMaker()
payment = MoneyMachine()

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        break
    elif user_input == 'report':
        coffee.report()
        payment.report()
    else:
        drink = menu_item.find_drink(user_input)
        if drink:
            if coffee.is_resource_sufficient(drink):
                if payment.make_payment(drink.cost):
                    coffee.make_coffee(drink)


