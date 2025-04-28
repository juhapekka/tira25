import itertools

def count_numbers(length, numbers):
    # TODO
    # hmm..?
    #return len(list(itertools.combinations_with_replacement(numbers, length)))
    return sum(1 for c in itertools.combinations_with_replacement(numbers, length) if not (length > 1 and c[0] == '0'))


if __name__ == "__main__":
    print(count_numbers(3, "123")) # 10
    print(count_numbers(5, "1")) # 1
    print(count_numbers(2, "137")) # 6
    print(count_numbers(8, "25689")) # 495
    print(count_numbers(1, "0")) # 1
    print(count_numbers(2, "0")) # 0
    print(count_numbers(10, "12")) # 11
    print(count_numbers(10, "123456789")) # 43758

    print(count_numbers(2, '0')) # 0