def count_splits(numbers):
    setti = set(numbers)
    unik = dict.fromkeys(setti, 0)
    namo = len(unik.keys())

    for i in numbers:
        unik[i] += 1

    passed = dict.fromkeys(setti, 0)
    count = 0
    lunik = 0

    for i in numbers:
        if passed[i] == 0:
            passed[i] += 1
            lunik += 1

        unik[i] -= 1
        if unik[i] == 0:
            return count
        
        if lunik == namo:
            count += 1

    return count


if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1