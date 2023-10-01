from console_gfx import *


def print_menu():  # prints menu
    print('RLE Menu\n'
          '--------\n'
          '0. \nExit\n'
          '1. Load File\n'
          '2. Load Test Image\n'
          '3. Read RLE String\n'
          '4. Read RLE Hex String\n'
          '5. Read Data Hex String\n'
          '6. Display Image\n'
          '7. Display RLE String\n'
          '8. Display Hex RLE Data\n'
          '9. Display Hex Flat Data\n')

def execute_user_input():  # this function prompts the user for an input. The function loop will continue to execute until the input is 0
    prompt = 'Select a menu option: '
    user_input = int(input(prompt))
    while user_input != 0:
        if user_input == 1:
            filename = input('Enter name of file to load: ')
            image = ConsoleGfx.load_file(filename)
        elif user_input == 2:
            image = ConsoleGfx.test_image
            print('Test image data loaded: ')
        elif user_input == 6:  # Display image
            ConsoleGfx.display_image(image)

        print()
        print_menu()
        user_input = int(input(prompt))


print('Welcome to the RLE image encoder!')  # Welcome message

print('Displaying Spectrum Image: ')
rainbow = ConsoleGfx.test_rainbow  # display the rainbow
ConsoleGfx.display_image(rainbow)

print_menu()
execute_user_input()