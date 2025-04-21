# materiaaleista https://tira.mooc.fi/kevat-2025/osa15/#union-find-rakenne
from collections import defaultdict
from copy import deepcopy

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

# materiaaleista https://tira.mooc.fi/kevat-2025/osa15/#kruskalin-algoritmi
class Kruskal:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def construct(self):
        self.edges.sort(key=lambda x: x[2])

        uf = UnionFind(self.nodes)
        edges_count = 0
        tree_weight = 0

        for edge in self.edges:
            node_a, node_b, weight = edge
            if uf.find(node_a) != uf.find(node_b):
                uf.union(node_a, node_b)
                edges_count += 1
                tree_weight += weight

        if edges_count != len(self.nodes) - 1:
            return None
        return tree_weight

class SameWeight:
    def __init__(self, n):
        self.n = n
        self.edget = []

    def add_edge(self, a, b, x):
        # TODO
        self.edget.append((a, b, x))



    def check(self):
        # TODO

        def paino(ylosalas):
            k = Kruskal(range(1, self.n + 1))
            if ylosalas:
                for a, b, w in self.edget:
                    k.add_edge(a, b, -w)
                w_neka = k.construct()
                return None if w_neka is None else -w_neka
            else:
                for a, b, w in self.edget:
                    k.add_edge(a, b, w)
                return k.construct()

        return paino(False) == paino(True)


if __name__ == "__main__":
    same_weight = SameWeight(4)

    same_weight.add_edge(1, 2, 2)
    same_weight.add_edge(1, 3, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(1, 4, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(3, 4, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(2, 4, 1)
    print(same_weight.check()) # False
