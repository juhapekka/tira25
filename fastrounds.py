def count_rounds(numbers):
    rr = 1
    numba = len(numbers)
    lista = numbers
    index_map = {num: idx for idx, num in enumerate(lista)}
    
    for i in range(1, numba):
        if index_map[i + 1] < index_map[i]:
            rr += 1
            
    return rr

def count_rounds2(numbers):
    rr = 0
    numba = 1
    lista = numbers
    def ninright(lastindex):
        nonlocal numba 
        nonlocal rr 
        nonlocal lista 

        indexi = lista.index(numba)
        if indexi < lastindex:
            rr += 1
            return
        numba += 1
        ninright(indexi)
        
    while numba in numbers:
        ninright(numbers)

    return rr            

if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000
