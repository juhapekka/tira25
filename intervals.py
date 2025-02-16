import random

def count_nested(intervals):
    # alun mukaan nouseva
    # sama alku, lopun mukaan laskeva
    intervals_sorted = sorted(intervals, key=lambda x: (x[0], -x[1]))

    nestaus = 0
    maksimi_end = -float('inf')

    for (a, b) in intervals_sorted:
        # tää b <= maksimi_end, (a,b) nähdyn välin sisällä.
        if b <= maksimi_end:
            nestaus += 1
        else:
            maksimi_end = b

    return nestaus


if __name__ == "__main__":
    print(count_nested([])) # 0
    print(count_nested([(1, 2)])) # 0
    print(count_nested([(1, 2), (3, 4)])) # 0
    print(count_nested([(1, 3), (2, 4)])) # 0
    print(count_nested([(1, 4), (2, 3)])) # 1
    print(count_nested([(1, 4), (1, 3)])) # 1
    print(count_nested([(1, 4), (2, 4)])) # 1
    print(count_nested([(1, 1), (1, 2), (1, 3)])) # 2
    print(count_nested([(1, 6), (2, 5), (3, 4)])) # 2
    print(count_nested([(1, 4), (2, 5), (3, 6)])) # 0

    intervals = [(x+1, x+3) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 0

    intervals = [(x+1, 2*10**5-x) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 99999