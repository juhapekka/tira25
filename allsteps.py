def count_steps(x):
    result = {1: 1}

    for n in range(1, x + 1):
        if n in result:
            for uusi in (n + 3, n * 2):
                if uusi <= x:
                    result[uusi] = result.get(uusi, 0) + result[n]
    return result.get(x, 0)

if __name__ == "__main__":
    print(count_steps(1)) # 1
    print(count_steps(2)) # 1
    print(count_steps(3)) # 0
    print(count_steps(4)) # 2
    print(count_steps(5)) # 1
    print(count_steps(17)) # 5
    print(count_steps(42)) # 0
    print(count_steps(100)) # 242
    print(count_steps(1000)) # 2948311