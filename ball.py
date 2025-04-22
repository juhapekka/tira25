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

class Ball:
    def __init__(self, n):
        # TODO
        self.n = n
        self.parit = set() # (kumpula, viikki)

    def add_pair(self, a, b):
        # TODO
        self.parit.add((a, b))

    def max_pairs(self):
        # TODO
        alkusolmu = 0
        loppusolmu = 2 * self.n + 1

        kumpula = list(range(1, self.n + 1))
        viikki = list(range(self.n + 1, 2 * self.n + 1))

        mf = MaximumFlow([alkusolmu] + kumpula + viikki + [loppusolmu])

        # alku->kumpulasolmut
        for k in kumpula:
            mf.add_edge(alkusolmu, k, 1)

        # parit k v
        for k, v in self.parit:
            mf.add_edge(k, self.n + v, 1)

        # viikkisolmut->loppu
        for v in viikki:
            mf.add_edge(v, loppusolmu, 1)

        return mf.construct(alkusolmu, loppusolmu)

if __name__ == "__main__":
    ball = Ball(4)

    print(ball.max_pairs()) # 0

    ball.add_pair(1, 2)
    print(ball.max_pairs()) # 1

    ball.add_pair(1, 3)
    ball.add_pair(3, 2)
    print(ball.max_pairs()) # 2

    ball.add_pair(2, 1)
    print(ball.max_pairs()) # 3
