# materiaaleista https://tira.mooc.fi/kevat-2025/osa15/#union-find-rakenne

class UnionFind:
    def __init__(self, nodes):
        self.link = {node: None for node in nodes}
        self.size = {node: 1 for node in nodes}

    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]


class MaxSet:
    def __init__(self, n):
        # TODO
        self.n = n
        self.uf = UnionFind(range(1, n + 1))
        self.koko = 1

    def merge(self, a, b):
        # TODO
        _a = self.uf.find(a)
        _b = self.uf.find(b)

        #print(f"{_a == _b}")
        # eri juures
        if _a != _b:
            koko_a = self.uf.size.get(_a, 0)
            koko_b = self.uf.size.get(_b, 0)

            self.uf.union(_a, _b)
            self.koko = max(self.koko, koko_a + koko_b)

    def get_max(self):
        return self.koko

if __name__ == "__main__":
    max_set = MaxSet(5)
    print(max_set.get_max()) # 1

    max_set.merge(1, 2)
    max_set.merge(3, 4)
    max_set.merge(3, 5)
    print(max_set.get_max()) # 3

    max_set.merge(1, 5)
    print(max_set.get_max()) # 5

    max_set.merge(2, 3)
    print(max_set.get_max()) # 5
