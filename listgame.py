def first_wins(numbers):
    # TODO
    n = len(numbers)
    taulu = [[numbers[i] if i == j else 0 for j in range(n)] for i in range(n)]
    #print(taulu)

    for ll in range(2, n + 1):
        for i in range(0, n - ll + 1): ###

            j = i + ll - 1

            # x -- o
            # |
            # v       
            v  = numbers[i] - taulu[i + 1][j]
            o = numbers[j] - taulu[i][j - 1]
            taulu[i][j] = max(v, o)
            #print(taulu)

    #print(taulu[0])
    return taulu[0][n - 1] > 0

if __name__ == "__main__":
    print(first_wins([2, 1, 3])) # True
    
    print(first_wins([1, 3, 1])) # False
    """
    print(first_wins([1])) # True
    print(first_wins([1, 1])) # False
    print(first_wins([1, 5])) # True
    print(first_wins([1, 1, 1])) # True
    print(first_wins([1, 2, 3, 4])) # True
    print(first_wins([1, 3, 3, 7, 4, 2, 1])) # False

    print(first_wins([1] * 50)) # False
    print(first_wins([1, 2] * 25)) # True
    """