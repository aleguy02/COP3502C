def octal_string_decode(oct, n=-1, total=0):
    digit_list = []
    for _digit_ in octal_num:  # I need to separate the input into its digits to do the calculations
        digit_list.append(_digit_)
    digit_list.reverse()  # reversing the order lets me increment n to correctly match the digit place
    for digit in digit_list:
        digit = int(digit)
        n += 1
        num_added = digit * 8 ** n
        total += num_added
    return total


if __name__ == '__main__':  # used to pass unit test on zybooks
    octal_num = input()
    total = octal_string_decode(octal_num)
    print(total)
