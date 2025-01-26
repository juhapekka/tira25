def find_segments(data):
    lista = []

    cc = 0
    bc = ''
    for c in data:
        if bc != c:
            if bc != '':
                lista.append((cc, bc))

            cc = 0
            bc = c
        
        cc += 1

    if cc > 0:
        lista.append((cc, bc))


    return lista

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]