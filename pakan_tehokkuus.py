import time
import collections

lista = collections.deque()

def lisaa(lista, n):
    for i in range(n):
        lista.append(i)

def poista(lista, n):
    for i in range(n):
        lista.popleft()


alku = time.time()
_ = lisaa(lista, 1000000)
loppu = time.time()
print(f"time: {loppu - alku:.6f} s")


alku = time.time()
_ = poista(lista, 1000000)
loppu = time.time()
print(f"time: {loppu - alku:.6f} s")