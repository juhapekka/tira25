class AllPaths:
    def __init__(self, n):
        self.n = n
        self.noodit = list(range(1, n + 1))
        self.graph = {x: [] for x in self.noodit}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def count(self):    
        polut = 0

        def count_paths(graph, u):
            polut = 1
            for v in graph.get(u, []):
                polut += count_paths(graph, v)
            return polut

        for noodi in self.noodit:
            polut += count_paths(self.graph, noodi)

        return polut


if __name__ == "__main__":
    counter = AllPaths(4)

    counter.add_edge(1, 2)
    counter.add_edge(1, 3)
    counter.add_edge(2, 4)
    counter.add_edge(3, 4)

    print(counter.count()) # 10

    counter.add_edge(2, 3)

    print(counter.count()) # 14
