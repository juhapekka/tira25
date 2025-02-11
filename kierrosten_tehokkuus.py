import time

def count_rounds_list(numbers):
    n = len(numbers)

    rounds = 1
    for i in range(1, n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1

    return rounds

def count_rounds_list_vk2(numbers):
    n = len(numbers)
    pos = [0] * (n+1)

    for i in range(n):
        pos[numbers[i]] = i

    rounds = 1
    for number in range(2, n+1):
        if pos[number] < pos[number - 1]:
            rounds += 1

    return rounds

def count_rounds_dict(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds

lista = list(range(1, 10**7))

"""
# does not finish timely

alku = time.time()
_ = count_rounds_list(lista)
loppu = time.time()
print(f"list time: {loppu - alku:.6f} s")
"""

alku = time.time()
_ = count_rounds_list_vk2(lista)
loppu = time.time()
print(f"list time: {loppu - alku:.6f} s")

alku = time.time()
_ = count_rounds_dict(lista)
loppu = time.time()
print(f"dict time: {loppu - alku:.6f} s")


