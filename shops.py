def find_distances(street):
    n = len(street)
    matkat = [n] * n

    # etäisyys vasemmalta
    if street[0] == '1':
        matkat[0] = 0

    # eka matka jää maximiksi jos 0
    for i in range(1, n):
        if street[i] == '1':
            matkat[i] = 0
        else:
            matkat[i] = matkat[i - 1] + 1

    # takaperin .. katotaan oikealta ja otetaan pienimmät matkat
    for i in range(n - 2, -1, -1):
        matkat[i] = min(matkat[i], matkat[i + 1] + 1)

    return matkat

if __name__ == "__main__":
    print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]

    n = 10**5
    street = "0"*n + "1" + "0"*n
    distances = find_distances(street)
    print(distances[1337]) # 98663