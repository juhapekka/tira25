def count_splits(sequence):
    if sequence.count('0') != sequence.count('1'):
        return 0

    c = 0
    nollat = 0
    ykkoset = 0
    
    for i in range(len(sequence) - 1):
        if sequence[i] == '0':
            nollat += 1
        else:
            ykkoset += 1
        
        # tasapainossa
        if nollat == ykkoset:
            c += 1
            
    return c

if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999