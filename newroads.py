#materiialeista https://tira.mooc.fi/kevat-2025/osa15/#union-find-rakenne

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


class NewRoads:
    def __init__(self, n):
        # TODO
        self.n = n
        self.lisatyt_tiet = []


    def add_road(self, a, b, x):
        # TODO
        self.lisatyt_tiet = sorted(self.lisatyt_tiet + [(a, b, x)], key=lambda tie: tie[2])

    def min_cost(self):
        # TODO
        uf = UnionFind(range(1, self.n + 1))
        rval = 0
        edge_co = 0

        for tie in self.lisatyt_tiet:
            city_a, city_b, paino = tie

            if uf.find(city_a) != uf.find(city_b):
                uf.union(city_a, city_b)
                rval += paino
                edge_co += 1

        if edge_co == self.n - 1:
            return rval
        else:
            return -1

if __name__ == "__main__":
    new_roads = NewRoads(4)

    new_roads.add_road(1, 2, 2)
    new_roads.add_road(1, 3, 5)
    print(new_roads.min_cost()) # -1

    new_roads.add_road(3, 4, 4)
    print(new_roads.min_cost()) # 11

    new_roads.add_road(2, 3, 1)
    print(new_roads.min_cost()) # 7
