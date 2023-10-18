from console_gfx import *


def print_menu():  # prints menu
    print('RLE Menu\n'
          '--------\n'
          '0. Exit\n'
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
    prompt = 'Select a Menu Option: '
    user_input = int(input(prompt))
    while user_input != 0:
        if user_input == 1:
            filename = input('Enter name of file to load: ')
            image = ConsoleGfx.load_file(filename)
        elif user_input == 2:
            image = ConsoleGfx.test_image
            print('Test image data loaded.')
        elif user_input == 3:
            data = input('Enter an RLE string to be decoded: ')
            current_data = string_to_rle(data)  # encodes RLE
            current_data = decode_rle(current_data)  # flattens RLE
        elif user_input == 4:
            data = input('Enter the hex string holding RLE data: ')
            current_data = string_to_data(data)  # encodes RLE
            current_data = decode_rle(current_data)  # flattens RLE
        elif user_input == 5:
            data = input('Enter the hex string holding flat data: ')
            current_data = string_to_data(data)  # encodes data
        elif user_input == 6:  # Display image
            print('Displaying image...')
            ConsoleGfx.display_image(image)
        elif user_input == 7:
            current_data = encode_rle(current_data)
            print(f'RLE representation: {to_rle_string(current_data)}')
        elif user_input == 8:
            current_data = encode_rle(current_data)
            print(f'RLE hex values: {to_hex_string(current_data)}')
        elif user_input == 9:
            print(f'Flat hex values: {to_hex_string(current_data)}')

        print()
        print_menu()
        user_input = int(input(prompt))

# 1
dec_to_hex = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
}
def to_hex_string(data: list, hex_string=''):
    """Translates data (RLE or raw) a hexadecimal string (without delimiters). """
    for i in data:
        i = dec_to_hex[i]
        hex_string += i
    return hex_string

# 2
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

# 3
def encode_rle(flat_data: list):
    """Returns encoding (in RLE) of the raw data passed in; used to generate RLE representation of a data."""
    encoded_data = []
    prev_val = flat_data[0]
    run_length = 0
    for i, val in enumerate(flat_data):
        if run_length == 15:
            encoded_data.extend([run_length, prev_val])
            run_length = 0
        # if data values change (curval != prevval), insert the length of the current run and prevval into encoded data list in that order
        if prev_val != val and run_length != 0:
            encoded_data.extend([run_length, prev_val])
            run_length = 0
        prev_val = val
        run_length += 1
    encoded_data.extend([run_length, prev_val])
    return encoded_data

# 4
def get_decoded_length(rle_data):
    total_length = 0
    # add the length value of each run to length
    for length in rle_data[::2]:
        total_length += length
    return total_length

#5
def decode_rle(rle_data):
    """Returns the decoded data set from RLE encoded data. This decompresses RLE data for use."""
    decoded_rle = []
    index = 0
    for val in (rle_data[1::2]):
        # rle_data[index] = run length for current value
        for i in range(rle_data[index]):
            decoded_rle.append(val)

        index = index + 2
    return decoded_rle

# 6
hex_to_dec = {value: key for key, value in dec_to_hex.items()}  # inverted dictionary woaAHHHHHH
hex_to_dec['A'] = 10
hex_to_dec['B'] = 11
hex_to_dec['C'] = 12
hex_to_dec['D'] = 13
hex_to_dec['E'] = 14
hex_to_dec['F'] = 15

def string_to_data(data_string):
    """Translates a string in hexadecimal format into byte data (can be raw or RLE)"""
    formatted_list = []
    for letter in data_string:
        letter = hex_to_dec[letter]
        formatted_list.append(letter)
    return formatted_list


# 7
def to_rle_string(rle_data: list):
    string_rle = ''
    index = 0
    for val in (rle_data[1::2]):
        # rle_data[index] = run length for current value
        string_rle += str(rle_data[index]) + dec_to_hex[val] + ':'
        index += 2
    return string_rle[:-1]

# 8
def string_to_rle(rle_string: str):
    rle_data = []
    rle_string_list = rle_string.split(':')
    for val in rle_string_list:
        rle_data.extend([int(val[:-1]), hex_to_dec[val[-1]]])
    return rle_data

if __name__ == '__main__':
    print('Welcome to the RLE image encoder!')  # Welcome message
    print()
    print('Displaying Spectrum Image:')
    rainbow = ConsoleGfx.test_rainbow  # display the rainbow
    ConsoleGfx.display_image(rainbow)
    print()
    print()

    print_menu()
    execute_user_input()