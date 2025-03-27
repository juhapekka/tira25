def find_sequence(numbers):
    # TODO
    n = len(numbers)
    pituudet = [1] * n
    rev = [-1] * n
    max_ll = 0
    max_llindex = 0

    for i in range(n):
        for j in range(i):
            if numbers[j] < numbers[i] and pituudet[j] + 1 > pituudet[i]:
                pituudet[i] = pituudet[j] + 1
                rev[i] = j
        if pituudet[i] > max_ll:
            max_ll = pituudet[i]
            max_llindex = i

    rval = []
    i = max_llindex
    while i != -1:
        rval.append(numbers[i])
        i = rev[i]

    rval.reverse()
    return rval

if __name__ == "__main__":
    print(find_sequence([1, 2, 3])) # [1, 2, 3]
    print(find_sequence([3, 2, 1])) # [1]
    print(find_sequence([1, 1, 1, 1, 1])) # [1]

    print(find_sequence([1, 8, 2, 7, 3, 6])) # [1, 2, 3, 6]
    print(find_sequence([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find_sequence([4, 1, 5, 6, 3, 4, 3, 8])) # [1, 3, 4, 8]