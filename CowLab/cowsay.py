import sys
from heifer_generator import HeiferGenerator
from cow import Cow

if __name__ == '__main__':
    if sys.argv[1] == '-l':  # function 1
        print('Cows available: ', end='')
        for index in range(len(HeiferGenerator.cowNames)):
            print(HeiferGenerator.cowNames[index], end=' ')
    elif sys.argv[1] == '-n':  # function 3
        c = Cow(sys.argv[2])
        MESSAGE = ''
        for i in range(3, len(sys.argv)):
            MESSAGE += sys.argv[i] + ' '
        if c.name in HeiferGenerator.cowNames:
            c_index = HeiferGenerator.cowNames.index(c.name)
            print(MESSAGE)
            print(HeiferGenerator.quoteLines, end='')
            print(HeiferGenerator.cowImages[c_index])
        else:
            print(f'Could not find {c.name} cow!')
    elif sys.argv[1]:  # prints out the MESSAGE using the default COW
        # function 2
        MESSAGE = ''
        for i in range(1, len(sys.argv)):
            MESSAGE += sys.argv[i] + ' '
        print(MESSAGE)
        print(HeiferGenerator.quoteLines, end='')
        print(HeiferGenerator.cowImages[0])


