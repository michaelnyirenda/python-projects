from resources import coffee, machine
def report(resource):
    """Generates report that shows the current resource values"""
    return f"Water: {resource['water']}ml \n" \
           f"Milk: {resource['milk']}ml \n" \
           f"Coffee: {resource['coffee']}g\n" \
           f"Money: ${resource['money']}"

def stock(drink):
    """Checks if there is enough resources in the machine"""

    for i in drink:
        if drink[i] >= machine[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def payment():
    """Calculates the total amount of coins"""
    print("Please insert coins")
    total = float(input("How many quarters?")) * 0.25
    total += float(input("How many dimes?")) * 0.10
    total += float(input("How many nickels?")) * 0.05
    total += float(input("How many pennies?")) * 0.01
    return total

def transaction(money_recieved, drink_cost):
    """Returns true if the payment was accepted, or false if the money is insufficient."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change")
        machine["money"] += drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink, ingredients):
    """Deduct the required ingredients from the machine resources"""
    for i in ingredients:
        machine[i] -= ingredients[i]
    print(f"Here is your {drink}")


is_on = True

while is_on:
    bev = input("What would you like? (espresso/latte/cappuccino): ")
    if bev == "off":
        is_on = False
    elif bev == "report":
        print(report(machine))
    else:
        drink = coffee[bev]
        if stock(drink["ingredients"]):
            paid = payment()
            if transaction(paid, drink["cost"]):
                make_coffee(bev, drink["ingredients"])
