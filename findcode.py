import re, itertools

class Oracle:
    def __init__(self, code):
        self.code = code
        self.counter = 0

    def check_code(self, code):
        self.counter += 1
        if self.counter > 16:
            raise RuntimeError("too many check_code calls")

        if type(code) != str or not re.match("^[1-9]{4}$", code) or len(code) != len(set(code)):
            raise RuntimeError("invalid code for check_code")

        in_place = in_code = 0
        for pos in range(4):
            if code[pos] in self.code:
                if code[pos] == self.code[pos]:
                    in_place += 1
                else:
                    in_code += 1

        return in_place, in_code

def _filtteri(arvaus, ss):
    paikka = sum(g == s for g, s in zip(arvaus, ss))
    kode  = sum(g in ss for g in arvaus) - paikka
    return paikka, kode

def find_code(oracle):
    # TODO
    c = [''.join(p) for p in itertools.permutations("123456789", 4)]
    while True:
        vastaus = oracle.check_code(c[0])
        if vastaus == (4, 0):
            return c[0]

        c = [code for code in c if _filtteri(c[0], code) == vastaus]

if __name__ == "__main__":
    # esimerkki oraakkelin toiminnasta
    oracle = Oracle("4217")
    print(oracle.check_code("1234")) # (1, 2)
    print(oracle.check_code("3965")) # (0, 0)
    print(oracle.check_code("4271")) # (2, 2)
    print(oracle.check_code("4217")) # (4, 0)

    # esimerkki funktion find_code toiminnasta
    oracle = Oracle("4217")
    code = find_code(oracle)
    print(code) # 4217

    oracle = Oracle("9861")
    code = find_code(oracle)
    print(code) # 4217
