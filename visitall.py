import itertools

def find_route(distances):
    # TODO
    n = len(distances)

    min_matka = float("inf")
    paras_reitti = []

    for p in itertools.permutations(range(2, n + 1)):
        taa_matka = 0
        reitin_nodet = [1] + list(p) + [1]

        for i in range(n):
            u = reitin_nodet[i]
            v = reitin_nodet[i+1]
            taa_matka += distances[u-1][v-1]

        if taa_matka < min_matka:
            min_matka = taa_matka
            paras_reitti = reitin_nodet

    return min_matka, paras_reitti



if __name__ == "__main__":
    distances = [[0, 2, 2, 1, 8],
                 [2, 0, 9, 1, 2],
                 [2, 9, 0, 8, 3],
                 [1, 1, 8, 0, 3],
                 [8, 2, 3, 3, 0]]

    length, route = find_route(distances)
    print(length) # 9
    print(route) # [1, 3, 5, 2, 4, 1]

    distances = [[0, 7, 5, 9, 6, 3, 1, 3],
                 [7, 0, 3, 2, 3, 3, 7, 8],
                 [5, 3, 0, 4, 2, 7, 7, 1],
                 [9, 2, 4, 0, 2, 3, 2, 4],
                 [6, 3, 2, 2, 0, 9, 5, 9],
                 [3, 3, 7, 3, 9, 0, 4, 5],
                 [1, 7, 7, 2, 5, 4, 0, 7],
                 [3, 8, 1, 4, 9, 5, 7, 0]]

    length, route = find_route(distances)
    print(length) # 18
    print(route) # [1, 7, 4, 6, 2, 5, 3, 8, 1]
