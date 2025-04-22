#materiaaleista https://tira.mooc.fi/kevat-2025/osa16/#ford-fulkerson-algoritmi
class MaximumFlow:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_edge(self, node_a, node_b, capacity):
        self.graph[(node_a, node_b)] += capacity

    def add_flow(self, node, sink, flow):
        if node in self.seen:
            return 0
        self.seen.add(node)
        if node == sink:
            return flow
        for next_node in self.nodes:
            if self.flow[(node, next_node)] > 0:
                new_flow = min(flow, self.flow[(node, next_node)])
                inc = self.add_flow(next_node, sink, new_flow)
                if inc > 0:
                    self.flow[(node, next_node)] -= inc
                    self.flow[(next_node, node)] += inc
                    return inc
        return 0

    def construct(self, source, sink):
        self.flow = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            add = self.add_flow(source, sink, float("inf"))
            if add == 0:
                break
            total += add
        return total

class Planets:
    def __init__(self, n):
        # TODO
        self.n = n
        self.linkit = []

    def add_teleport(self, a, b):
        # TODO
        self.linkit.append((a, b))


    def min_removals(self):
        # TODO
        a = 1
        b = self.n
        mf = MaximumFlow(range(1, self.n + 1))

        for _a, _b in self.linkit:
            mf.add_edge(_a, _b, 1)

        return mf.construct(a, b)


if __name__ == "__main__":
    planets = Planets(5)

    print(planets.min_removals()) # 0

    planets.add_teleport(1, 2)
    planets.add_teleport(2, 5)
    print(planets.min_removals()) # 1

    planets.add_teleport(1, 5)
    print(planets.min_removals()) # 2
