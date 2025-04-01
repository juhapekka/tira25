def find_first(size, steps):
    # TODO
    if size % 2 == 1:  # pariton
        jaksot = (size + 1) // 2
        setp_eff = steps % jaksot
        rval = 2 * setp_eff + 1
    else:  # parillinen
        jaksot = size
        setp_eff = steps % jaksot
        if setp_eff < size // 2:
            rval = 2 * setp_eff + 1
        else:
            j = setp_eff - (size // 2)
            rval = 2 * (j + 1)


    return rval

if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295
    print(find_first(123456789, 1337**42)) # 111766959
