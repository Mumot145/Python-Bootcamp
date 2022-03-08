# Hi! My Name is Patrick Mumot. I am learning Python :)

# Here is my coffee Machine from my journey in the 100 Day challenge!

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0.0
profit_description = "${:,.2f}".format(profit)

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def display_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit_description}")


def is_correct_choice(choice):
    if choice == "espresso" or choice == "latte" or choice == "cappuccino" :
        return True
    else:
        return False


def collect_coins(coffee):
    print(f"Please insert " + "${:,.2f}".format(coffee))
    total = int(input("How many Quarters:")) * 0.25
    total += int(input("How many Dimes:")) * 0.1
    total += int(input("How many Nickels:")) * 0.05
    total += int(input("How many Pennies:")) * 0.01
    return total


def resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def payment_sufficient(order_payment, cost):
    if order_payment >= cost:
        change = round(order_payment - cost, 2)
        global profit
        profit += order_payment
        print(f"Here is your change: " + "${:,.2f}".format(change))
        return True
    else:
        print("Not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


isOn = True


while isOn:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        exit()
    elif choice == "report":
        display_report()
    elif is_correct_choice(choice):
        drink = MENU[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = collect_coins(drink["cost"])
            if payment_sufficient(payment, drink["cost"]):
                print(f"Here is your {choice}. Thank you, come again!")
                make_coffee(choice, drink["ingredients"])
