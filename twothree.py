import heapq

def find_smallest(steps):
    dadad = [1]
    nahdyt = {1}

    for _ in range(steps):
        x = heapq.heappop(dadad)
        x2 = x * 2
        x3 = x * 3

        #print("---")
        #print(x2)
        #print(x3)

        if x2 not in nahdyt:
            nahdyt.add(x2)
            heapq.heappush(dadad, x2)

        if x3 not in nahdyt:
            nahdyt.add(x3)
            heapq.heappush(dadad, x3)

    return dadad[0]    

if __name__ == "__main__":
    print(find_smallest(0)) # 1
    print(find_smallest(1)) # 2
    print(find_smallest(2)) # 3
    print(find_smallest(3)) # 4
    print(find_smallest(4)) # 6
    print(find_smallest(5)) # 8

    print(find_smallest(42)) # 1296
    print(find_smallest(1337)) # 16210220612075905068
    print(find_smallest(123123)) # 47241633171870338440585357243035120029747450090811731814934867117962334088709324512562801224664331563355142646399182644605958987116029586018592281978123083613432358051028210559768563023872
