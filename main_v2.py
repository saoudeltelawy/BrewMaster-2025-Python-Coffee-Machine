from art import logo
from data import brewMaster_resources, MENU

print(logo)
print("Welcome to BrewMaster 2025, your personal coffee machine!")
# print(data.machine_resources)

# -- Initials -- :
total_money = 0  # Tracks the user’s inserted money for a single transaction
change = 0  # Tracks the remaining money to return to the user
collected_money = 0  # Tracks the total revenue collected by the machine
powered_on = True  # A flag to keep the machine running.


def machine_resources(brewMaster_resources):
    """Formats and returns a report of the current resources in the machine (water, milk, coffee beans, and money(Revenue))"""
    return (
        f" {brewMaster_resources['water']} ml of Water\n"
        f"{brewMaster_resources['milk']} ml of Milk\n"
        f"{brewMaster_resources['coffee_beans']} g of Coffee beans\n"
        f"${brewMaster_resources['money']} of Money"
    )


# -  Print Machine Resources for the first time!
print(f"Initial Machine Resources:\n{machine_resources(brewMaster_resources)}")


# Main Program Loop
while powered_on:
    # No Resources is the first condition to check & turn off the machine VIP
    if (
        brewMaster_resources["water"] <= 0
        or brewMaster_resources["milk"] <= 0
        or brewMaster_resources["coffee_beans"] <= 0
    ):
        print("Machine has run out of resources. Turning off.")
        powered_on = False
        break
    # User Friendly Menu
    print("\n=== Menu ===")
    for drink in MENU:
        print(f"{drink.capitalize()}: ${MENU[drink]['cost']}")
    print()  # Prints a blank line
    # Gather User Choice!
    user_choice = input(
        "What would you like to dink ☕? (espresso/latte/cappuccino): "
    ).lower()

    # Report Section
    if user_choice == "report":
        # Collected Money in the report section
        brewMaster_resources["money"] = collected_money
        print(
            machine_resources(brewMaster_resources)
        )  # Dynamically get updated resources
        # Turn off the machine
    elif user_choice == "off":
        powered_on = False
        print(
            f"Machine is powered off and the Total Money Collected: ${collected_money}"
        )
        print("Goodbye! ... Have a nice day!")
    # Normal Operation/Process:
    elif user_choice in MENU:
        # - Money Insertion
        print(f"Please insert coins.")
        # Gather Money!!!
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total_money += quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        print(f"Here is ${round(total_money, 2)} in change.")
        # Check if enough money and if there is a change for the user!
        if total_money < MENU[user_choice]["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
            total_money = 0
            print(f"Total Money in the machine now is ${total_money}.")
            change = 0
            powered_on = False
        else:
            # First of all to Check if resources are sufficient to start drink ==== # Check if resources are sufficient BEFORE deduction
            if (
                brewMaster_resources["water"]
                >= MENU[user_choice]["ingredients"]["water"]
                and brewMaster_resources["milk"]
                >= MENU[user_choice]["ingredients"].get(
                    "milk", 0
                )  # Default to 0 if "milk" doesn't exist
                and brewMaster_resources["coffee_beans"]
                >= MENU[user_choice]["ingredients"]["coffee"]
            ):
                # Then for Resources  --> If sufficient, deduct the resources
                brewMaster_resources["water"] -= MENU[user_choice]["ingredients"][
                    "water"
                ]
                brewMaster_resources["milk"] -= MENU[user_choice]["ingredients"].get(
                    "milk", 0
                )
                brewMaster_resources["coffee_beans"] -= MENU[user_choice][
                    "ingredients"
                ]["coffee"]

                change += total_money - MENU[user_choice]["cost"]
                print(f"Your change is ${round(change, 2)}.")
                # - If enough money, make the coffee [Successful Transaction]:
                print(f"Here is your {user_choice} ☕. Enjoy!")
                total_money = 0
                collected_money += MENU[user_choice]["cost"]
                change = 0  # Reset change for the next transaction

            else:
                print("Sorry, there is not enough resources.")
                print(
                    f"The current machine resources are:\n{machine_resources(brewMaster_resources)}"
                )
                powered_on = False
    else:
        print("Invalid choice. Please try again.")


# Finally, Print Total Money Collected per day!
print(f"Total Money Collected: ${collected_money}")