hex_value = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


dec_to_hex = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


def hex_char_decode(digit):
    """decodes single digit hex value into its decimal value"""
    digit = digit.upper()
    return hex_value[digit]


def hex_string_decode(hex, n=0, total=0):
    """decodes a hex string into its decimal value"""
    digit_list = []

    if hex[0] == '0' and hex[1] == 'x':  # the hex value has to be stripped of the prefix '0x' before being passed
        hex = hex[2:]

    for digit in hex:  # all digits in hex are converted to their decimal value and added to a list
        digit = digit.upper()  # all letters in the hex number are capitalized so that it matches the key
        digit = hex_value[digit]
        digit_list.append(digit)

    digit_list.reverse()  # reverse the list
    for digit in digit_list:  # decimal value = hex_last_digit * 16**0 + hext_next_digit * 16**1...
        decimal_value = digit * 16**n
        total += decimal_value
        n += 1

    return total


def binary_string_decode(binary, n=0, total=0):
    """decodes a binary string into its decimal value"""
    digit_list = []

    if binary[0] == '0' and binary[1] == 'b':
        binary = binary[2:]

    for _digit_ in binary:  # I need to separate the input into its digits to do the calculations
        digit_list.append(_digit_)
    digit_list.reverse()  # reversing the order lets me increment n where to correctly match the digit place
    for digit in digit_list:
        digit = int(digit)
        num_added = digit * 2 ** n
        total += num_added
        n += 1
    return total


def binary_to_hex(binary, total=0):
    digit_list = []
    dec = binary_string_decode(binary)
    next_val = dec
    while True:
        if next_val == 0:
            break  # this line and all the previous are original code/ideas

        remainder = next_val % 16  # All I learned with the internet was that I needed these variables and how to create them
        next_val = next_val // 16  # All I learned with the internet was that I needed these variables and how to create them

        remainder = dec_to_hex[remainder]  # this line and all the following are original code/ideas
        digit_list.append(remainder)
    digit_list.reverse()
    hex_code = ''
    for digit in digit_list:
        hex_code += digit
    return hex_code


def print_menu():
    print('Decoding Menu\n'
          '-------------\n'
          '1. Decode hexadecimal\n'
          '2. Decode binary\n'
          '3. Convert binary to hexadecimal\n'
          '4. Quit')


if __name__ == '__main__':
    while True:
        print_menu()
        choice = int(input('Please enter an option: '))
        if choice == 4:
            print('Goodbye!')
            break
        numeric_string = input('Please enter the numeric string to convert: ')

        if choice == 1 and len(numeric_string) == 1:
            result = hex_char_decode(numeric_string)
        elif choice == 1:
            result = hex_string_decode(numeric_string)
        elif choice == 2:
            result = binary_string_decode(numeric_string)
        elif choice == 3:
            result = binary_to_hex(numeric_string)

        print('Result: ', result)
