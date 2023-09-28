dec_to_hex = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


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
    while True:  # Admittedly, I got stuck on how to convert from decimal to hex, so I googled JUST so I could get the ball rolling
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


test_num = 10011111
print(binary_to_hex(test_num))