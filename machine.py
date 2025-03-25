def min_steps(x):
    result = {1: 0}

    for n in range(1, x + 1):
        if n in result:
            for uusi in (n + 3, n * 2):
                if uusi <= x:
                    result[uusi] = min(result.get(uusi, 1000), result[n] + 1)
    return result.get(x, -1)

if __name__ == "__main__":
    print(min_steps(1)) # 0
    print(min_steps(2)) # 1
    print(min_steps(3)) # -1
    print(min_steps(4)) # 1
    print(min_steps(5)) # 2
    print(min_steps(17)) # 4
    print(min_steps(42)) # -1
    print(min_steps(100)) # 7
    print(min_steps(1000)) # 13