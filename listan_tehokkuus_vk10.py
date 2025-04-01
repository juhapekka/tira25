import time
import random
import heapq

def eka(lista):
    summa = sum(sorted(lista)[:len(lista) // 10])
    return summa

def toka(lista):
    keko = []

    for x in lista:
        heapq.heappush(keko, x)

    n = len(lista)
    pienimmat = [heapq.heappop(keko) for _ in range(n // 10)]

    summa = sum(pienimmat)
    return summa

def kolmas(lista):
    heapq.heapify(lista)
    n = len(lista)
    summa = sum(heapq.heappop(lista) for _ in range(n // 10))
    return summa

lista = [random.randint(1, 10**9) for _ in range(10**7)]


alku = time.time()
_ = eka(lista)
loppu = time.time()
print(f"1.time: {loppu - alku:.6f} s")


alku = time.time()
_ = toka(lista)
loppu = time.time()
print(f"2.time: {loppu - alku:.6f} s")

alku = time.time()
_ = kolmas(lista)
loppu = time.time()
print(f"3.time: {loppu - alku:.6f} s")
