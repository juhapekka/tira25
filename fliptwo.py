import collections

def find_first(size, steps):
    # TODO
    d = collections.deque(range(1, size + 1))

    for _ in range(steps):
        a = d.popleft() # eka
        b = d.popleft() # toka
        d.append(b)
        d.append(a)

    return d[0]

if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295