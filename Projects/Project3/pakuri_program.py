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


# 1
def main_list_pakuri(pakudex):
    if pakudex.get_species_array():
        print('Pakuri In Pakudex:')
        for i, pakuri in enumerate(pakudex.get_species_array()):
            print(f'{i + 1}. {pakuri}')
    else:
        print('No Pakuri in Pakudex yet!')


# 2
def main_show_pakuri(pakudex):
    pakuri = input('Enter the name of the species to display: ')
    try:
        if pakuri in pakudex.get_species_array():
            index = (pakudex.get_species_array().index(pakuri))
            pakuri_obj = pakudex.species_array[index]
            stats = pakudex.get_stats(pakuri_obj)
            print(
                f'Species: {pakuri}\n'
                f'Attack: {stats[0]}\n'
                f'Defense: {stats[1]}\n'
                f'Speed: {stats[2]}'
            )
        else:
            raise TypeError
    except TypeError:
        print('Error: No such Pakuri!')


# 3
def main_add_pakuri(pakudex):
    if pakudex.size >= pakudex.capacity:
        print('Error: Pakudex is full!')
    else:
        species_name = input('Enter the name of the species to add: ')
        pakuri = Pakuri(species_name)
        pakudex.add_pakuri(pakuri)


# 4
def main_evolve_pakuri(pakudex):
    pakuri = input('Enter the name of the species to evolve: ')
    if pakuri in pakudex.get_species_array():
        index = (pakudex.get_species_array().index(pakuri))
        pakuri_obj = pakudex.species_array[index]
        pakudex.evolve_species(pakuri_obj)
        print(f'{pakuri} has evolved!')
    else:
        print('Error: No such Pakuri!')


# 5
def main_sort_pakuri(pakudex):
    pakudex.sort_pakuri()
    print('Pakuri have been sorted!')


if __name__ == "__main__":
    welcome()
    capacity = set_capacity()
    pakudex = Pakudex(capacity)

    _input = -1
    while _input != 6:
        print_menu()
        try:  # the main logic will go here ig
            _input = int(input('What would you like to do? '))
            if not 0 < _input <= 6:
                raise ValueError

            if _input == 1:
                main_list_pakuri(pakudex)
            elif _input == 2:
                main_show_pakuri(pakudex)
            elif _input == 3:
                main_add_pakuri(pakudex)
            elif _input == 4:
                main_evolve_pakuri(pakudex)
            elif _input == 5:
                main_sort_pakuri(pakudex)
            elif _input == 6:
                print('Thanks for using Pakudex! Bye!')
        except ValueError:
            print('Unrecognized menu selection!')
