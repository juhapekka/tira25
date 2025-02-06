def count_sublists(numbers):
    if not numbers:
        return 0

    rval = 0
    current_length = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            current_length += 1
        else:
            rval += current_length * (current_length + 1) // 2
            current_length = 1

    rval += current_length * (current_length + 1) // 2
    return rval

if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4])) # 7
    print(count_sublists([1, 2, 3, 4])) # 10
    print(count_sublists([4, 3, 2, 1])) # 4
    print(count_sublists([1, 1, 1, 1])) # 4
    print(count_sublists([1, 2, 1, 2])) # 6

    numbers = list(range(1, 10**5+1))
    print(count_sublists(numbers)) # 5000050000