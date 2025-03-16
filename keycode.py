def find_codes(pattern):
    rval = []
    nahdyt = set()
    koodi = [None, None, None, None]

    n = len(pattern)
    if n != 4:
        return

    def valkkeri(i):
        if i == n:
            rval.append("".join(str(x) for x in koodi))
            return

        if pattern[i] == '?':            
            for d in range(1, 10): # 1..9, ei nollaa
                if d not in nahdyt:
                    nahdyt.add(d)
                    koodi[i] = d
                    valkkeri(i + 1)
                    nahdyt.remove(d)
                    #print(nahdyt)
        else:
            d = int(pattern[i])
            if d in nahdyt:
                return
    
            nahdyt.add(d)
            koodi[i] = d
            valkkeri(i + 1)
            nahdyt.remove(d) # <--- !

    valkkeri(0)
    return rval



if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024