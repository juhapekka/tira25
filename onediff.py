def count_strings(n):
    # TODO
    if n <= 0: # 0 => 0
        return 0
    if n == 1: # 1 => 26
        return 26
    
    maarat = [1] * 26

    for _ in range(2, n + 1):
        uus = [0] * 26

        for i in range(26):
            if i == 0:
                uus[i] = maarat[1]
            elif i == 25:
                uus[i] = maarat[24]
            else:
                uus[i] = maarat[i - 1] + maarat[i + 1]
        maarat = uus

    return sum(maarat)


if __name__ == "__main__":
    print(count_strings(1)) # 26
    print(count_strings(2)) # 50
    print(count_strings(3)) # 98
    print(count_strings(4)) # 192

    print(count_strings(42)) # 36766943673096
    print(count_strings(100)) # 7073450400109633000218032957656