def count_numbers(a, b):
    numbat = []

    def generoi(num):
            if num > b:
                return
            
            if num != 0:
                numbat.append(num)
            
            for digit in (2, 5):
                generoi(num * 10 + digit)
    generoi(0)

    return sum(1 for num in numbat if a <= num <= b)

def count_numbers3(a, b):
    cc = 0
    numbat = {'2', '5'}
    for m in range(a, b + 1):
        ss = str(m)
        if all(ch in numbat for ch in ss):
            cc += 1

    return cc


def count_numbers2(a, b):
    cc = 0
    numbat = [2, 5]
    for m in range(a, b + 1):
        divdiv = 1
        res = 1
        while m // divdiv:
            nn = (m // divdiv) % 10
            if nn not in numbat:
                res = 0
                break
            divdiv *= 10
        cc += res
    return cc
        

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512
