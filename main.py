from ingredients import MENU, resources

total_money = 0
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


def report():
    water_amount = resources["water"]
    print(f"Water = {water_amount}ml")
    milk_amount = resources["milk"]
    print(f"Milk = {milk_amount}ml")
    coffee_amount = resources["coffee"]
    print(f"Coffee = {coffee_amount}g")
    print(f"${total_money}")


def coffee_type():
    if ask == 'espresso':
        change = sum - 1.50
        global total_money
        total_money += 1.50
        print(f"Your change is: ${round(change, 2)}")
        if change < 0:
            print("Insufficient Funds")
    elif ask == 'latte':
        change = sum - 2.50
        total_money += 2.50
        print(f"Your change is: ${round(change, 2)}")
        if change < 0:
            print("Insufficient Funds")
    elif ask == 'cappuccino':
        change = sum - 3.50
        total_money += 3.50
        print(f"Your change is: ${round(change, 2)}")
        if change < 0:
            print("Insufficient Funds")
    else:
        exit()


def subtract_resources():
    global resources

    if ask == 'espresso':
        required_resources = {"water": 50, "coffee": 18}
    elif ask == 'latte':
        required_resources = {"water": 200, "milk": 150, "coffee": 24}
    elif ask == 'cappuccino':
        required_resources = {"water": 250, "milk": 100, "coffee": 24}
    else:
        print("Invalid choice")
        return False

    for resource, amount in required_resources.items():
        resources[resource] -= amount
    return True


keep_purchasing = True

while keep_purchasing:
    ask = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if ask == 'off':
        exit()

    if ask != 'report':
        print("Please insert coins.")

        quarters_amount = float(input("How many quarters?: "))
        dimes_amount = float(input("How many dimes?: "))
        nickels_amount = float(input("How many nickels?: "))
        pennies_amount = float(input("How many pennies?: "))

        sum = (quarters_amount * QUARTERS) + (dimes_amount * DIMES) + (nickels_amount * NICKLES) + (
                pennies_amount * PENNIES)

        coffee_type()


        if not subtract_resources():
            print("Transaction failed due to insufficient resources.")
            break


    else:
        report()













