hex_value = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


def hex_char_decode(digit):
    """decodes single digit hex value into its decimal value"""
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


_input = input()
decoded_total = hex_string_decode(_input)
print(decoded_total)
