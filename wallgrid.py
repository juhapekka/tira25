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

class WallGrid:
    def __init__(self, n):
        # TODO
        self.n = n
        self.uf = UnionFind([])
        self.lattia = set()
        self.huoneet = 0

    def create_floor(self, x, y):
        # TODO
        if (x, y) in self.lattia:
            return
        naapurit = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        i = (x - 1) * self.n + y

        self.uf.link[i] = None
        self.uf.size[i] = 1
        self.lattia.add((x, y))
        self.huoneet += 1

        for dx, dy in naapurit:
            nx = x + dx
            ny = y + dy
            if not (1 <= nx <= self.n and 1 <= ny <= self.n):
                continue
            if (nx, ny) not in self.lattia:
                continue

            naapuri = (nx - 1) * self.n + ny

            if self.uf.find(i) != self.uf.find(naapuri):
                self.uf.union(i, naapuri)
                self.huoneet -= 1

    def count_rooms(self):
        # TODO
        return self.huoneet

if __name__ == "__main__":
    wall_grid = WallGrid(5)

    print(wall_grid.count_rooms()) # 0

    wall_grid.create_floor(2, 2)
    wall_grid.create_floor(4, 2)
    print(wall_grid.count_rooms()) # 2

    wall_grid.create_floor(3, 2)
    print(wall_grid.count_rooms()) # 1

    wall_grid.create_floor(2, 4)
    wall_grid.create_floor(2, 4)
    wall_grid.create_floor(4, 4)
    print(wall_grid.count_rooms()) # 3

    wall_grid.create_floor(3, 3)
    print(wall_grid.count_rooms()) # 3

    wall_grid.create_floor(3, 4)
    print(wall_grid.count_rooms()) # 1
