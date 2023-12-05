def bubble_sort(unsorted_list, size):
    for i in range(0, size):
        num = 0
        for j in range(1, size):
            if unsorted_list[num] > unsorted_list[j]:
                temp = unsorted_list[num]
                unsorted_list[num] = unsorted_list[j]
                unsorted_list[j] = temp
            num += 1
        size -= 1


if __name__ == "__main__":
    size = int(input())
    unsorted_list = []
    for i in range(0, size):
        num = int(input())
        unsorted_list.append(num)
    bubble_sort(unsorted_list, size)
    print(unsorted_list)