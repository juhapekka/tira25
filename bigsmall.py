def count_pairs(numbers):
    numnum = sorted(numbers)
    n = len(numbers)

    ala = 0
    yla = n // 2
    parit = 0

    while ala < n // 2 and yla < n:
        if 2 * numnum[ala] <= numnum[yla]:
            parit += 1
            ala += 1
            yla += 1
        else:
            yla += 1

    return parit



if __name__ == "__main__":
    print(count_pairs([1])) # 0
    print(count_pairs([1, 2, 3])) # 1
    print(count_pairs([1, 2, 3, 4])) # 2
    print(count_pairs([1, 1, 1, 1])) # 0
    print(count_pairs([10**9, 1, 1, 1])) # 1
    print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
    print(count_pairs([1, 2, 3, 2, 4, 6])) # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers)) # 41176