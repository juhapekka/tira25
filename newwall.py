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



def min_changes(grid):
    # TODO

    n = len(grid)

    def id(r, c, type):
        return 1 + (r * n + c) * 2 + type

    kaikki_id = set([0, 1 + ( (n-1)*n + (n-1) ) * 2 + 1 + 1]) #alku,loppu
    #print(kaikki_id)
    edget = [] # (u, v, ww)

    for r in range(n):
        for c in range(n):
            if grid[r][c] != '#':
                n1_id = id(r, c, 0)
                n2_id = id(r, c, 1)
                kaikki_id.add(n1_id)
                kaikki_id.add(n2_id)

                w = float('inf') if ((r == 0 and c == 0) or (r == n - 1 and c == n - 1)) else 1
                edget.append((n1_id, n2_id, w))

                if c + 1 < n and grid[r][c+1] != '#':
                    naapuri1_id = id(r, c + 1, 0)
                    edget.append((n2_id, naapuri1_id, float('inf')))
                if r + 1 < n and grid[r+1][c] != '#':
                    naapuri1_id = id(r + 1, c, 0)
                    edget.append((n2_id, naapuri1_id, float('inf')))

    #print("-----\n" + str(kaikki_id))
    #print("-----\n" + str(edget))

    mf = MaximumFlow(list(kaikki_id))

    for u, v, w in edget:
        mf.add_edge(u, v, w)

    return mf.construct(id(0, 0, 1), id(n - 1, n - 1, 0))




if __name__ == "__main__":
    grid = ["...#.",
            "...#.",
            "####.",
            ".....",
            "....."]

    print(min_changes(grid)) # 0

    grid = [".#...",
            "...#.",
            "...#.",
            ".###.",
            ".###."]

    print(min_changes(grid)) # 0

    grid = [".#...",
            "...#.",
            "...#.",
            ".###.",
            "....."]

    print(min_changes(grid)) # 1

    grid = [".....",
            ".###.",
            "...#.",
            "##.#.",
            "....."]

    print(min_changes(grid)) # 2
