import random
import time

# toteutus 1
def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# toteutus 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)


lista = [random.randint(0, 100) for _ in range(10**7)]

alku = time.time()
_ = count_even1(lista)
loppu = time.time()
print(f"time: {loppu - alku:.6f} s")

alku = time.time()
_ = count_even2(lista)
loppu = time.time()
print(f"time: {loppu - alku:.6f} s")