import sys
from heifer_generator import HeiferGenerator
from cow import Cow
from dragon import Dragon
from ice_dragon import IceDragon

if __name__ == '__main__':
    if sys.argv[1] == '-l':  # function 1
        print('Cows available: ', end='')
        for index in range(len(HeiferGenerator.cow_names)):
            print(HeiferGenerator.cow_names[index], end=' ')
        for index in range(len(HeiferGenerator.dragon_names)):
            print(HeiferGenerator.dragon_names[index], end=' ')

    elif sys.argv[1] == '-n':  # function 3
        name = sys.argv[2]
        MESSAGE = ''
        for i in range(3, len(sys.argv)):
            MESSAGE += sys.argv[i] + ' '

        if name in HeiferGenerator.cow_names:
            c = Cow(name)
            c_index = HeiferGenerator.cow_names.index(c.name)
            c.set_image(HeiferGenerator.cowImages[c_index])
            print(MESSAGE)
            print(HeiferGenerator.quote_lines, end='')
            print(c.get_image())
        elif name in HeiferGenerator.dragon_names:
            d = IceDragon(name, HeiferGenerator.dragon_image)
            print(MESSAGE)
            print(HeiferGenerator.quote_lines, end='')
            print(d.get_image())
            print('This dragon can breathe fire.') if d.can_breathe_fire() else print('This dragon cannot breathe fire.')
        else:
            print(f'Could not find {name} cow!')

    elif sys.argv[1]:  # prints out the MESSAGE using the default COW
        # function 2
        MESSAGE = ''
        for i in range(1, len(sys.argv)):
            MESSAGE += sys.argv[i] + ' '
        print(MESSAGE)
        print(HeiferGenerator.quote_lines, end='')
        print(HeiferGenerator.cowImages[0])