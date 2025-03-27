def count_sequences(numbers):
    # TODO
    n = len(numbers)
    if n == 0:
        return 0

    pituudet = [1] * n
    maarat = [1] * n

    for i in range(n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                if pituudet[j] + 1 > pituudet[i]:
                    pituudet[i] = pituudet[j] + 1
                    maarat[i] = maarat[j]
                elif pituudet[j] + 1 == pituudet[i]:
                    maarat[i] += maarat[j]

    #print(maarat)
    #print(pituudet)

    return sum(maarat[i] for i in range(n) if pituudet[i] == max(pituudet))

if __name__ == "__main__":
    print(count_sequences([1, 2, 3])) # 1
    print(count_sequences([3, 2, 1])) # 3
    print(count_sequences([1, 1, 1, 1, 1])) # 5

    print(count_sequences([1, 8, 2, 7, 3, 6])) # 1
    print(count_sequences([1, 1, 2, 2, 3, 3])) # 8
    print(count_sequences([4, 1, 5, 6, 3, 4, 3, 8])) # 3