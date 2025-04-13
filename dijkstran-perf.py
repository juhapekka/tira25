import time
import random
import heapq

class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))

    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0

        queue = []
        heapq.heappush(queue, (0, start_node))

        visited = set()
        while queue:
            node_a = heapq.heappop(queue)[1]
            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)

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

    bf = Dijkstra(nodet)

    for edge in edget:
        bf.add_edge(edge[0], edge[1], edge[2])

    print(f"find_distances(..)...")
    alku = time.time()
    _ = bf.find_distances(1)
    loppu = time.time()

    print(f"bf.find_distances aika: {loppu - alku:.6f} s")
