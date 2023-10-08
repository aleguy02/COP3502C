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


dec_to_hex = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
}
def to_hex_string(data: list, hex_string=''):
    for i in data:
        i = dec_to_hex[i]
        hex_string += i
    return hex_string


def count_runs(flat_data: list):
    '''loop through flat_data until the index value changes (this signifies the end of a run)
    runs can be 15 pixels long MAX'''
    num_runs = 1
    prev_val = flat_data[0]
    run_length = 0
    for val in flat_data:
        if run_length > 15:  # if run length is greater than 15, increment number of runs and make a new run
            num_runs += 1
            run_length = 0
        # in order to determine if the index value changes, store the previous index value then compare it with the current index value
        # if the values are the same, do nothing and move on to the next value in the list
        if val != prev_val:  # if the values change (prev_val is different from current val), add 1 to num_runs
            num_runs += 1
            run_length = 0
        prev_val = val  # the run ends when the value changes. We can keep track of this by storing the previous list val in a variable
        # increment run length by 1 for every loop
        run_length += 1
    return num_runs


def encode_rle(flat_data: list):
    '''count the length of the run, then put the length, value of the run into the next 2 spots of a list. Do this for an entire
    set of data'''
    encoded_data = []
    prev_val = flat_data[0]
    run_length = 0
    for i, val in enumerate(flat_data):
        if run_length == 15:
            encoded_data.extend([run_length, prev_val])
            run_length = 0
        # if data values change (curval != prevval), insert the length of the current run and prevval into encoded data list in that order
        if prev_val != val:
            encoded_data.extend([run_length, prev_val])
            run_length = 0
        prev_val = val
        run_length += 1
    encoded_data.extend([run_length, prev_val])
    return encoded_data


print('Welcome to the RLE image encoder!')  # Welcome message

print('Displaying Spectrum Image: ')
rainbow = ConsoleGfx.test_rainbow  # display the rainbow
ConsoleGfx.display_image(rainbow)

print_menu()
execute_user_input()