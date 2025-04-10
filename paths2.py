# materiaaleista https://tira.mooc.fi/kevat-2025/osa13/#dynaaminen-ohjelmointi
class CountPaths:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def count_from(self, node):
        if node in self.result:
            return self.result[node]

        path_count = 0
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)

        self.result[node] = path_count
        return path_count

    def count_paths(self, x, y):
        self.result = {y: 1}
        return self.count_from(x)
    

def create_edges(x):
    edget = []
    n = 100
    
    pot_alku = 2
    pot_loppu = 33

    for i in range(pot_alku, pot_loppu + 1):
        for j in range(i + 1, pot_loppu + 1):
            edget.append((i, j))

    edget.append((pot_loppu, 100))

    for p in range(31): # 2^30 > 10^9
        # x !!
        if (x >> p) & 1:
            noodi = 32 - p
            if pot_alku <= noodi < pot_loppu:
                 if (1, noodi) not in edget:
                      edget.append((1, noodi))
            else: 
                print(f"ffail {noodi} pot {p}")

    #rval = list(set(edget))
    #print(rval)
    #if len(rval) != len(edget):
    #    print(f"ffail {len(rval)} -- {len(edget)}")
    return edget #rval


if __name__ == "__main__":
    edges = create_edges(123456789)

    counter = CountPaths(range(1, 100 + 1))
    for edge in edges:
        counter.add_edge(edge[0], edge[1])
    print(counter.count_paths(1, 100)) # 123456789
