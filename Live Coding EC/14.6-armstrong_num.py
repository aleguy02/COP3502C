a, b = input().split()

for i in range(int(a), int(b) + 1):
    current_instance = str(i)
    armstrong_num = 0
    n = len(current_instance)
    for digit in current_instance:
        armstrong_num = armstrong_num + pow(int(digit), n)
    if i == armstrong_num:
        print(armstrong_num)

# Lisa's way
a, b = input().split()
a, b = int(a), int(b)  # a =500, b = 10000

for i in range(a, b + 1):
    # look at i = 500, 501, 502, ..., 10000
    # look at specific number 678
    # 1. how many digits: n
    num_digits = 0
    temp = i
    while temp > 0:
        last_digit = temp % 10
        num_digits += 1
        temp //= 10

    # 2. look at each digit, raise that digit to n, sum
    total = 0
    temp = i
    while temp > 0:
        last_digit = temp % 10
        total += last_digit ** num_digits  # 8^3 + 7^3 + 6^3
        temp //= 10

    if total == i:
        print(total)
