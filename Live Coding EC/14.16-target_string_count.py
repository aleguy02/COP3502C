def target_string_count(s, target):
    if target not in s:
        return 0
    else:
        index = s.index(target)
        index_end = s.index(target) + len(target)
        new_string = s[:index] + s[index_end:]
        return target_string_count(new_string, target) + 1


if __name__ == '__main__':
    s, target = input().split(' ')
    print(target_string_count(s, target))