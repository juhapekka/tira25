def create_words(word):
    rval = []
    sana = []

    n = len(word)
    ww = {}
    for c in word:
        if c not in ww.keys():
            ww[c] = 1
        else:
            ww[c] += 1


    def valkkeri():
        if len(sana) == len(word):
            rval.append("".join(sana))
            return

        vika_c = sana[-1] if sana else None
        for c in ww.keys():
            if ww[c] > 0 and c != vika_c:
                ww[c] -= 1
                sana.append(c)
                valkkeri()
                sana.pop()
                ww[c] += 1

    valkkeri()
    return sorted(rval)

if __name__ == "__main__":
    print(create_words("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create_words("aab")) # ['aba']
    print(create_words("aaab")) # []

    print(create_words("kala"))
    # ['akal', 'akla', 'alak', 'alka', 'kala', 'laka']

    print(create_words("syksy"))
    # ['ksysy', 'kysys', 'skysy', 'syksy', 'sykys', 'sysky', 
    #  'sysyk', 'yksys', 'ysksy', 'yskys', 'ysyks', 'ysysk']

    print(len(create_words("aybabtu"))) # 660
    print(len(create_words("abcdefgh"))) # 40320