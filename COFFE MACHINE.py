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
def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry, that product is too much.")
            return False
    return True
def process_coins():
    print("Hey! I'm thinking of a coin. can you insert coins")
    total = int(input("haw many quarters?:")) * 0.25
    total += int(input("haw many dimes?:")) * 0.1
    total += int(input("haw many nickles?:")) * 0.05
    total += int(input("haw many pennies?:")) * 0.01
    return total
def is_transaction_successful(money_recived,drink_cost):
    if money_recived >= drink_cost:
        change = round(drink_cost - money_recived,2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money.")
        return False
def make_coffe(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} coffe!")
is_one = True
while is_one:
    choice = input("What type of coffe do you like (cappuccino,latte,expresso)>>>")
    if choice == "off":
        is_one = False
    elif choice == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee:{resources['coffee']}")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])