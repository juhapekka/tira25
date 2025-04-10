class GraphGame:
    def __init__(self, n):
        self.n = n
        self.noodit = list(range(1, n + 1))
        self.graph = {i: [] for i in self.noodit}


    def add_link(self, a, b):
        self.graph[a].append(b)


    def winning(self, x):
        naapurit = self.graph.get(x, [])

        for v in naapurit:
            if not self.winning(v):
                return True

        return False


if __name__ == "__main__":
    game = GraphGame(6)

    game.add_link(3, 4)
    game.add_link(1, 4)
    game.add_link(4, 5)

    print(game.winning(3)) # False
    print(game.winning(1)) # False

    game.add_link(3, 1)
    game.add_link(4, 6)
    game.add_link(6, 5)

    print(game.winning(3)) # True
    print(game.winning(1)) # False
    print(game.winning(2)) # False