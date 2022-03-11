from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isOn = True

while isOn:
    choice = input("What would you like? (" + Menu.get_items() + "):")
    if choice == "off":
        exit()
    elif choice == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        coffee = Menu.find_drink(choice)
        if CoffeeMaker.is_resource_sufficient(coffee):
            money_paid = MoneyMachine.process_coins()
            if MoneyMachine.make_payment(money_paid):
                CoffeeMaker.make_coffee(coffee)


