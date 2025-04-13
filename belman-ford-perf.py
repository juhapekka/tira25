import time
import random

class BellmanFord:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0

        num_rounds = len(self.nodes) - 1
        for _ in range(num_rounds):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance

        return distances
    


if __name__ == "__main__":
    N = 5000

    nodet = list(range(1, N + 1))

    edget = []
    for a in nodet:
        for b in range(a + 1, min(N + 1, a + 10)):
            w = random.randint(1, 1000)
            edget.append((a, b, w))
    print(f"{len(edget)} edgeä")

    random.shuffle(edget)

    bf = BellmanFord(nodet)

    for edge in edget:
        bf.add_edge(edge[0], edge[1], edge[2])

    print(f"find_distances(..)...")
    alku = time.time()
    _ = bf.find_distances(1)
    loppu = time.time()

    print(f"bf.find_distances aika: {loppu - alku:.6f} s")
