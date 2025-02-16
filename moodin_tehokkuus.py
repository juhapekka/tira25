import time
import random

def find_mode_sort(numbers):
    nums = sorted(numbers)
    best_vv = nums[0]
    best_cc = 1

    taa_val = nums[0]
    taa_count = 1

    for i in range(1, len(nums)):
        if nums[i] == taa_val:
            taa_count += 1
        else:
            if taa_count > best_cc:
                best_vv = taa_val
                best_cc = taa_count

            taa_val = nums[i]
            taa_count = 1

    if taa_count > best_cc:
        best_vv = taa_val

    return best_vv

def find_mode_dict(numbers):
    laskurit = {}
    mode = numbers[0]  # säilytetään 'paras' moodi
    for x in numbers:
        if x not in laskurit:
            laskurit[x] = 0
        laskurit[x] += 1
        if laskurit[x] > laskurit[mode]:
            mode = x
    return mode


#lista = list(range(1, 10**7))
lista = [random.randint(1, 1000) for _ in range(10**7)]

alku = time.time()
_ = find_mode_sort(lista)
loppu = time.time()
print(f"find_mode_sort: {loppu - alku:.6f} s")


alku = time.time()
_ = find_mode_dict(lista)
loppu = time.time()
print(f"find_mode_dict: {loppu - alku:.6f} s")