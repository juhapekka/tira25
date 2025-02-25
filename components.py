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


def connected(nodes, edges):
    k = BellmanFord(nodes)
    for e in edges:
        k.add_edge(e[0], e[1], 1)
        k.add_edge(e[1], e[0], 1)
    
    for i in nodes:
        d = k.find_distances(i)

        if not any(value == float('inf') for value in d.values()):
            return True
    
    return False

def find_components(nodes, edges):
    k = BellmanFord(nodes)
    for e in edges:
        k.add_edge(e[0], e[1], 1)
        k.add_edge(e[1], e[0], 1)

    kaymaton = set(nodes)
    components = []

    while kaymaton:
        start = min(kaymaton)
        d = k.find_distances(start)

        c = [v for v in d if d[v] != float('inf')]
        c.sort()
        components.append(c)

        for x in c:
            kaymaton.remove(x)

    components.sort(key=lambda c: c[0])
    return components


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges)) # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges)) # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges)) # [[1, 2, 3, 4, 5]]