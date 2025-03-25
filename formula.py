import sys
sys.setrecursionlimit(5000)

def count_sequences(n):
    if n % 2 == 1:
        return 0

    k = n // 2
    c = 1
    for i in range(1, k + 1):
        c = c * (2 * k - i + 1) // i
    return c // (k + 1)

def count_sequences_slow2(n):
    if n % 2 == 1:
        return 0

    tall = {}
    
    def laske(jalj, d):
        if d < 0 or d > jalj:
            return 0
        if jalj == 0:
            return 1 if d == 0 else 0
        if (jalj, d) not in tall:
            tall[(jalj, d)] = laske(jalj - 1, d + 1) + laske(jalj - 1, d - 1)
        return tall[(jalj, d)]
    
    return laske(n, 0)

def count_sequences_slow(n):
    result = {}
    result[(0, 0)] = 1
    for i in range(1, n + 1):
        result[(0, i)] = 0
    for i in range(1, n + 1):
        for j in range(0, n + 1):
            result[(i, j)] = 0
            if j + 1 <= n:
                result[(i, j)] += result[(i - 1, j + 1)]
            if j - 1 >= 0:
                result[(i, j)] += result[(i - 1, j - 1)]
    return result[(n, 0)]

if __name__ == "__main__":
    print(count_sequences(1)) # 0
    print(count_sequences(2)) # 1
    print(count_sequences(3)) # 0
    print(count_sequences(4)) # 2
    print(count_sequences(5)) # 0
    print(count_sequences(6)) # 5

    print(count_sequences(42)) # 24466267020
    print(count_sequences(1000)) # 539497486917039060909410566119711128734834348196703167679426896420410037336371644508208550747509720888947317534973145917768881736628103627844100238921194561723883202123256952806711505149177419849031086149939116975191706558395784192643914160118616272189452807591091542120727401415762287153293056320