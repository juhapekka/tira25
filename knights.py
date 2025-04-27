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
    


def count_pairs(grid):
    # TODO
    n = 8
    ratsut = [(r, k) for r in range(n) for k in range(n) if grid[r][k] == '*']
    noodit = {(r, k): 1 + r * n + k for r, k in ratsut}
    siirrot = [ # dr dk
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    alkusolmu = 0
    loppusolmu = n * n + 1

    mf = MaximumFlow([alkusolmu] + list(noodit.values()) + [loppusolmu])

    for r1, k1 in ratsut:
        noodi1 = noodit[(r1, k1)]
        valkonen = (r1 + k1) % 2 == 0 # valkosella ruudulla
        #print(f"{noodi1} -- {valkonen}")

        if valkonen:
            mf.add_edge(alkusolmu, noodi1, 1)
            for dr, dk in siirrot:
                r2 = r1 + dr 
                k2 = k1 + dk

                # kaari valkosesta mustaan
                if 0 <= r2 < n and 0 <= k2 < n and grid[r2][k2] == '*':
                    noodi2 = noodit[(r2, k2)]
                    mf.add_edge(noodi1, noodi2, 1)
                    #print(f"{noodi1};{r1};{k1} -- {noodi2};{r2};{k2}")

        else: # musta
            mf.add_edge(noodi1, loppusolmu, 1)

    return mf.construct(alkusolmu, loppusolmu)

if __name__ == "__main__":
    grid = ["*.......",
            "..*...*.",
            "........",
            ".*......",
            "...*....",
            ".......*",
            "........",
            "......*."]

    print(count_pairs(grid)) # 3

    grid = ["*.***.**",
            "*******.",
            "*.**.**.",
            "***.****",
            "..****.*",
            "********",
            "*.******",
            "***.**.*"]

    print(count_pairs(grid)) # 25
