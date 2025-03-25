import itertools

def count_combinations(cards, target):
    # TODO
    rval = 0
    n = len(cards)

    for x in range(1, n + 1):
        for combo in itertools.combinations(cards, x):
            if sum(combo) == target:
                rval += 1

    return rval

if __name__ == "__main__":
    print(count_combinations([2, 1, 4, 6], 6)) # 2
    print(count_combinations([1, 1, 1, 1], 2)) # 6
    print(count_combinations([2, 1, 4, 6], 15)) # 0
    print(count_combinations([1], 1)) # 1
    print(count_combinations([1, 2, 3, 4, 5], 5)) # 3
    print(count_combinations([1, 1, 4, 1, 1], 4)) # 2
    print(count_combinations([1] * 10, 5)) # 252