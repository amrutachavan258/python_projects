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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry insufficient item {item}. ")
            return False
        return True

def process_coins():
    print("Enter the coins: ")
    total = 0
    total+=int(input("how many quarter? ")) * 0.25
    total+=int(input("how many dime? ")) * 0.10
    total+=int(input("how many nick? ")) * 0.05
    total+=int(input("how many penn? ")) * 0.01
    return total

def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change=money_received - drink_cost
        print("Your change is: ", change)
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry you don't have enough money")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Your {drink_name} is redy,enjoy it!")

is_on = True
while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: {profit} $")
    else:
        drink = MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



