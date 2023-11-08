from pakuri import Pakuri
from pakudex import Pakudex

def welcome():
    print('Welcome to Pakudex: Tracker Extraordinaire!')

def set_capacity():
    while True:
        try:
            capacity = int(input('Enter max capacity of the Pakudex: '))
            if capacity <= 0:
                raise Exception
            print(f'The Pakudex can hold {capacity} species of Pakuri.')
            break
        except:
            print('Please enter a valid size.')
    return capacity


def print_menu():
    print(
        'Pakudex Main Menu\n'
        '-----------------\n'
        '1. List Pakuri\n'
        '2. Show Pakuri\n'
        '3. Add Pakuri\n'
        '4. Evolve Pakuri\n'
        '5. Sort Pakuri\n'
        '6. Exit'
    )

welcome()
capacity = set_capacity()
print_menu()
print(capacity)