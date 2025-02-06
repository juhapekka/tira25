def count_sublists(numbers):
    rval = 0
    len = 0

    for number in numbers:
        if number % 2 == 0:
            len += 1
        else:
            # priton
            rval += len * (len + 1) // 2
            len = 0

    rval += len * (len + 1) // 2
    return rval

if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000