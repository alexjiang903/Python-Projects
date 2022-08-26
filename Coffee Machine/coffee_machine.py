from ingredients import MENU
from ingredients import resources

money = 0

user_choice = input('What would you like? Select one (Latte/Cappuccino/Espresso): ')
user_choice = user_choice.lower()


def coffee_machine():
    global user_choice
    global money

    if user_choice == 'report':
        water_left = resources["water"]
        milk_left = resources["milk"]
        coffee_left = resources["coffee"]

        print(f'Water: {water_left} ml')
        print(f'Milk: {milk_left} ml')
        print(f'Coffee: {coffee_left} g')
        print(f'Money: ${money}')

        user_choice = input('What would you like? Select one (Latte/Cappuccino/Espresso): ')
        user_choice = user_choice.lower()
        coffee_machine()

    elif user_choice == 'off':
        quit()

    drink_selected = MENU[user_choice]

    if resources['water'] <= 0:
        print('Sorry, we are out of water. Please try again later.')
        quit()

    elif resources['coffee'] <= 0:
        print('Sorry, we are out of coffee. Please try again later.')
        quit()

    elif user_choice != 'espresso' and resources['milk'] <= 0:
        print('Sorry, we are out of milk. Please try again later.')
        quit()

    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))

    total_paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    if total_paid < drink_selected["cost"]:
        print('Sorry that is not enough money. Money has been refunded.')
        user_choice = input('What would you like? Select one (Latte/Cappuccino/Espresso): ')
        user_choice = user_choice.lower()
        coffee_machine()
    else:
        if user_choice == 'espresso':
            resources['water'] -= MENU['espresso']['ingredients']['water']
            resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        else:
            resources['water'] -= drink_selected['ingredients']['water']
            resources['milk'] -= drink_selected['ingredients']['milk']
            resources['coffee'] -= drink_selected['ingredients']['coffee']

        change = total_paid - drink_selected['cost']

        if change != 0:
            print(f'Here is ${round(change, 2)} in change.')
            print(f'Your {user_choice} is served! Enjoy!')
            money += drink_selected['cost']
        elif change == 0:
            print(f'Your {user_choice} is served! Enjoy!')
            money += drink_selected['cost']


coffee_machine()

while user_choice != 'off':
    user_choice = input('What would you like? Select one (Latte/Cappuccino/Espresso): ')
    user_choice = user_choice.lower()
    coffee_machine()
