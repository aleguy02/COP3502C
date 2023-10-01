from console_gfx import *

prompt = 'Select a menu option: '
user_input = None
while user_input != 0:
    user_input = int(input(prompt))
    if user_input == 1:
        filename = input('Enter name of file to load: ')
        image = ConsoleGfx.load_file(filename)
    elif user_input == 2:
        image = ConsoleGfx.test_image
        print('Test image data loaded: ')
    elif user_input == 6:  # Display image
        ConsoleGfx.display_image(image)
