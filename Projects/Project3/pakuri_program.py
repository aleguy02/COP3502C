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
        '\nPakudex Main Menu\n'
        '-----------------\n'
        '1. List Pakuri\n'
        '2. Show Pakuri\n'
        '3. Add Pakuri\n'
        '4. Evolve Pakuri\n'
        '5. Sort Pakuri\n'
        '6. Exit'
    )

# 3
def main_add_pakuri():
    species_name = input('Enter the name of the species to add: ')
    pakuri = Pakuri(species_name)
    pakudex.add_pakuri(pakuri)



capacity = 5
pakudex = Pakudex(capacity)
