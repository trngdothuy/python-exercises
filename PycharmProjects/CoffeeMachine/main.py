MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

# TODO: 1. Print “What would you like? (espresso/latte/cappuccino):”

def check_resources():
    global water_needed, coffee_needed, milk_needed
    if water < water_needed:
        return 'Sorry there is not enough water.'
    elif milk < milk_needed:
        return 'Sorry there is not enough milk.'
    elif coffee < coffee_needed:
        return 'Sorry there is not enough coffee.'
    else:
        process_coin()

def remain(n1, n2):
    return n1 - n2

def process_coin():
    global selection, answer, money, water, milk, coffee, water_needed, coffee_needed, milk_needed, money_needed
    print("Please insert cọins.")
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if total < selection["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        water = remain(water, water_needed)
        milk = remain(milk, milk_needed)
        coffee = remain(coffee, coffee_needed)
        money += money_needed
        if  total > money_needed:
            change = str(round(total - money_needed, 2))
            print(f"Here is ${change} in change.")
        print(f"Here is your {answer} ☕. Enjoy!")

should_end = False
money = 0
water = int(resources["water"])
milk = int(resources["milk"])
coffee = int(resources["coffee"])
while not should_end:
    answer = input('What would you like? (espresso//latte/cappuccino):')
# TODO: 2. Turn off
    if answer == "off":
        should_end = True
# TODO: 3. Print report
    elif answer == "report":
        print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}')
# TODO: 4. Check resources
    elif answer == "espresso" or answer == "latte" or answer == "cappuccino":
        selection = MENU[answer]
        coffee_ingre = selection["ingredients"]
        water_needed = int(coffee_ingre["water"])
        coffee_needed = int(coffee_ingre["coffee"])
        milk_needed = int(coffee_ingre["milk"])
        money_needed = round(selection["cost"], 2)
        check_resources()
    else:
        should_end = False

# TODO: 5. Process coin
# TODO: 6. Check transaction
# TODO: 7. Make coffee


