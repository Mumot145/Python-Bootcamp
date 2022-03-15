from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isOn = True
coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while isOn:
    choice = input(f"What would you like? ({coffee_menu.get_items()}):")
    if choice == "off":
        exit()
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = coffee_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
