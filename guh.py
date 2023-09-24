hex_value = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


def hex_char_decode(digit):
    """decodes single digit hex value into its decimal value"""
    return hex_value[digit]


_input = input()
decoded_total = hex_char_decode(_input)
print(decoded_total)
