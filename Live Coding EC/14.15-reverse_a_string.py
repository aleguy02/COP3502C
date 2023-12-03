def reverse_string(string_to_reverse):
    if len(string_to_reverse) == 1 or len(string_to_reverse) == 0:
        return string_to_reverse
    if len(string_to_reverse) > 1:
        return reverse_string(string_to_reverse[1:]) + string_to_reverse[0]


if __name__ == '__main__':
    string_to_reverse = input()
    res = reverse_string(string_to_reverse)

    print(f'Reverse of "{string_to_reverse}" is "{res}".')
