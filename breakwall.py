# materiaaleista https://tira.mooc.fi/kevat-2025/osa14/#dijkstran-algoritmi

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


def find_route(grid):
    # TODO
    naapurit = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    noodit = [] #tupleina
    korkeus = len(grid)
    leveys = len(grid[0])


    for r in range(korkeus):
        for c in range(leveys):
            noodi = (r, c)
            noodit.append(noodi) #!
            if grid[r][c] == 'A':
                alku = noodi
            elif grid[r][c] == 'B':
                loppu = noodi
    #print(len(noodit))

    D = Dijkstra(noodit)

    for r in range(1, korkeus - 1):
        for c in range(1, leveys - 1):
            for dr, dc in naapurit:
                nr = r + dr
                nc = c + dc

                if grid[nr][nc] != '#':
                    if grid[nr][nc] == '*':
                        D.add_edge((r, c), (nr, nc), 1)
                    else:
                        D.add_edge((r, c), (nr, nc), 0)

    return D.find_distances(alku).get(loppu, -1)

if __name__ == "__main__":
    grid = ["########",
            "#*A*...#",
            "#.*****#",
            "#.**.**#",
            "#.*****#",
            "#..*.B.#",
            "########"]
    print(find_route(grid)) # 2