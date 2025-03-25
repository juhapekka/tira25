import itertools

def min_count(weights, max_weight):
    # TODO
    n = len(weights)
    if n == 0:
        return 0
    
    if any(w > max_weight for w in weights):
        return -1

    def jaettava(jaljella, laatikot):
        #print("-----")
        #print(jaljella)
        #print(laatikot)
        if jaljella == set():
            return True
        if laatikot == 0:
            return False
        
        for x in range(1, len(jaljella) + 1):
            for combo in itertools.combinations(jaljella, x):
                if sum(weights[i] for i in combo) <= max_weight:
                    uusijaljella = jaljella - set(combo)
                    if jaettava(uusijaljella, laatikot - 1):
                        return True
        return False

    for x in range(1, n + 1):
        if jaettava(set(range(n)), x):
            return x
    return -1


if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7)) # 2
    print(min_count([2, 3, 3, 5], 6)) # 3
    print(min_count([2, 3, 3, 5], 5)) # 3
    print(min_count([2, 3, 3, 5], 4)) # -1

    print(min_count([], 1)) # 0
    print(min_count([1], 1)) # 1
    print(min_count([1, 1, 1, 1], 1)) # 4
    print(min_count([1, 1, 1, 1], 4)) # 1

    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10)) # 3