def dec_to_octal(oct, decimal=''):
    digit_list = []
    next_value = oct
    while next_value > 0:
        remainder = next_value % 8
        next_value = next_value // 8
        digit_list.append(remainder)
    digit_list.reverse()
    for digit in digit_list:
        decimal += str(digit)
    return decimal

if __name__ == '__main__':
    octal_num = int(input())
    print(dec_to_octal(octal_num))
