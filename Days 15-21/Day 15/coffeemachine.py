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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# coins : 1ct, 10cts, 5cts,25 cts

def check_resources(drink,stock):
    required_water = int(drink['ingredients']['water'])
    if 'milk' in drink:
        required_milk = int(drink['ingredients']['milk'])
    else:
        required_milk = 0
    required_coffee = int(drink['ingredients']['coffee'])
    if required_coffee <= stock['coffee'] and required_milk <= stock['milk'] and required_water <= stock['water']:
        return True
    else:
        not_enough = []
        if required_coffee > stock['coffee']:
            not_enough.append("coffee")
        if required_milk > stock['milk']:
            not_enough.append("milk")
        if required_water > stock['water']:
            not_enough.append('water')
        print(f"Sorry there is not enough {not_enough}")
        return False

def print_report(stock,cash):
    water = stock['water']
    coffee = stock['coffee']
    milk = stock['milk']

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${cash}")

def add_coins(money,drink):
    more_money = True
    coins_worth = 0
    while more_money :
        cents = int(input("How many cents do you want to add"))
        dime = int(input("How many dimes do you want to add"))
        nickel = int(input("How many nickels do you want to add"))
        quarter = int(input("How many quarters do you want to add"))
        coins_worth += round((cents * 0.01) + (dime * 0.1) + (nickel * 0.05) + (quarter * 0.25),2)
        if coins_worth >= drink['cost']:
            more_money = False
        else:
            more_money = True
    return coins_worth


def make_drink(money,stock,drink):
    left_money = round(money - int(drink['cost']),2)
    required_water = int(drink['ingredients']['water'])
    if 'milk' in drink:
        required_milk = int(drink['ingredients']['milk'])
    else:
        required_milk = 0
    required_coffee = int(drink['ingredients']['coffee'])
    left_resources = {}
    left_resources['water'] = stock['water'] - required_water
    left_resources['milk'] = stock['milk'] - required_milk
    left_resources['coffee'] = stock['coffee'] - required_coffee
    return(left_money,left_resources)


money = 0

new_coffee = True

while new_coffee:
    ask = input("WHat would you like to have? (espresso/latte/cappuccino)\n")
    if ask == "off":
        new_coffee = False
    elif ask == "report":
        print_report(resources,money)
    else:
        drink=MENU[ask]
        resource_check = check_resources(drink,resources)
        if resource_check == True and money < drink['cost']:
            money = add_coins(money,drink)
            left = make_drink(money,resources,drink)
            money = left[0]
            resources = left[1]
            print_report(resources,money)
        elif resource_check == True and money > drink['cost']:
            left = make_drink(money,resources,drink)
            money = left[0]
            resources = left[0]
            print_report(resources,money)
        elif resource_check == False:
            print("Powering down")
            new_coffee = False
        else:
            print("error")


    


