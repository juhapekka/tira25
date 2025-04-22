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

class Download:
    def __init__(self, n):
        # TODO
        self.n = n
        self.linkit = []

    def add_link(self, a, b, x):
        # TODO
        self.linkit.append((a, b, x))


    def max_data(self, a, b):
        # TODO
        mf = MaximumFlow(range(1, self.n + 1))

        for _a, _b, _x in self.linkit:
            mf.add_edge(_a, _b, _x)

        return mf.construct(a, b)

if __name__ == "__main__":
    download = Download(4)

    print(download.max_data(1, 4)) # 0

    download.add_link(1, 2, 5)
    download.add_link(2, 4, 6)
    download.add_link(1, 4, 2)
    print(download.max_data(1, 4)) # 7

    download.add_link(1, 3, 4)
    download.add_link(3, 2, 2)
    print(download.max_data(1, 4)) # 8