def count_parts(songs):
    vika = {}
    ll = 0
    c = 0

    for right, song in enumerate(songs):
        if song in vika and vika[song] >= ll:
            ll = vika[song] + 1
        vika[song] = right

        c += (right - ll + 1)
        
    return c

if __name__ == "__main__":
    print(count_parts([1, 1, 1, 1])) # 4
    print(count_parts([1, 2, 3, 4])) # 10
    print(count_parts([1, 2, 1, 2])) # 7
    print(count_parts([1, 2, 1, 3])) # 8
    print(count_parts([1, 1, 2, 1])) # 6

    songs = [1, 2] * 10**5
    print(count_parts(songs)) # 399999
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs)) # 15000050000