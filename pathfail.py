import heapq


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
    
"""
1. Verkossa on n solmua, jotka on numeroitu 1,2,\dots,n.
    4..n ei ole kaaria, niihin vois lisätä nollapainoset


2. Saat päättää itse verkon kaarten määrän.
    ..
3. Jokainen kaari on suunnattu ja kaaren paino on kokonaisluku.
    .. yksi paino negatiivinen
4. Verkossa ei ole kahta kaarta samasta lähtösolmusta samaan kohdesolmuun.
    1->2, 2->3, 1->3, 3->n
    tai overflow kurkotetaan sen yli:
    1->2, 2->4, 4->3, 1->3, 3->n

5. Verkossa ei ole kaarta, jonka lähtösolmu ja kohdesolmu ovat samat.
    ..
6. Lyhimmän polun pituus solmusta 1 solmuun n on a, mutta Dijkstran algoritmi antaa vastauksen b.
    ..
"""
def create_edges_overflowfail(n, a, b):

    # nega kaari kunnolla nega
    x = -64738

    return [
        (1, 2, a - x),
        (2, 3, x),
        (1, 3, b),
        (3, n, 0),
    ]


RAJA = 10**9

def create_edges(n, a, b):
    # 1->3 menee rajoihin?
    if b <= RAJA - 1:
        r = b
        s = 0
    else:
        r = RAJA - 2
        s = b - r

    # x paino r + x + s + 1 = a
    x = a - s - r - 1
    if x == 0:
        x = -1 # nega

    if x < -RAJA: #negneg
        return [
            (1, 2, r + 1),
            (2, 4, x + RAJA),
            (4, 3, -RAJA),
            (1, 3, r),
            (3, n, s),
        ]
    else: # vain neg
        return [
            (1, 2, a - x),
            (2, 3, x),
            (1, 3, b),
            (3, n, 0),
        ]


def find_answer(my_class, n, edges):
    nodes = range(1, n + 1)
    finder = my_class(nodes)

    for edge in edges:
        finder.add_edge(edge[0], edge[1], edge[2])

    distances = finder.find_distances(1)
    return distances[n]

if __name__ == "__main__":
    n = 100
    edges = create_edges(n, 42, 1337)

    answer1 = find_answer(BellmanFord, n, edges)
    print(answer1) # 42

    answer2 = find_answer(Dijkstra, n, edges)
    print(answer2) # 1337

    n = 52
    edges = create_edges(n, 809409993, 977246705)
    answer1 = find_answer(BellmanFord, n, edges)
    print(answer1) # 809409993

    answer2 = find_answer(Dijkstra, n, edges)
    print(answer2) # 977246705
