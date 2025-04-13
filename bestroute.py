import heapq

# materiaaleista https://tira.mooc.fi/kevat-2025/osa14/#dijkstran-algoritmi
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

class BestRoute:
    def __init__(self, n):
        self.n = n
        self.noodit = list(range(1, n + 1))
        self.tiet = []



    def add_road(self, a, b, x):
        self.tiet.append((a, b, x))

        
    def find_route(self, a, b):
        bf = Dijkstra(self.noodit)

        for eka, toka, pituus in self.tiet:
            bf.add_edge(eka, toka, pituus)
            bf.add_edge(toka, eka, pituus)

        pituudet = bf.find_distances(a)
        rval = pituudet.get(b, float('inf'))
        return rval if rval != float('inf') else -1

if __name__ == "__main__":
    routes = BestRoute(3)

    routes.add_road(1, 2, 2)
    print(routes.find_route(1, 3)) # -1

    routes.add_road(3, 1, 5)
    print(routes.find_route(1, 3)) # 5

    routes.add_road(2, 3, 1)
    print(routes.find_route(1, 3)) # 3