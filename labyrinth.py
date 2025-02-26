# https://tira.mooc.fi/kevat-2025/osa8/#lyhimm%C3%A4t-polut-ja-et%C3%A4isyydet
class Distances:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def find_distances(self, start_node):
        distances = {}

        queue = [start_node]
        distances[start_node] = 0

        for node in queue:
            distance = distances[node]
            for next_node in self.graph[node]:
                if next_node not in distances:
                    queue.append(next_node)
                    distances[next_node] = distance + 1

        return distances

def find_route(grid):
    alku = None
    loppu = None
    mahd = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            ch = grid[r][c]
            if ch == 'A':
                alku = (r, c)
                mahd.append((r, c))
            elif ch == 'B':
                loppu = (r, c)
                mahd.append((r, c))
            elif ch == '.':
                mahd.append((r, c))
            # '#' ei tehä mitää

    d = Distances(mahd)

    # rakennetaan edget
    mahd_set = set(mahd)
    suunnat = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for (r, c) in mahd:
        for (dr, dc) in suunnat:
            rr, cc = r + dr, c + dc
            if (rr, cc) in mahd_set:
                d.add_edge((r, c), (rr, cc))

    try:
        return d.find_distances(alku)[loppu]
    except:
        return None


if __name__ == "__main__":
    grid1 = ["########",
             "#.#.B..#",
             "#A#.##.#",
             "#......#",
             "########"]
    print(find_route(grid1))  # 6

    grid2 = ["########",
             "#B#...A#",
             "#.#.##.#",
             "#......#",
             "########"]
    print(find_route(grid2))  # 9

    grid3 = ["########",
             "####..B#",
             "#.A#.#.#",
             "#..#...#",
             "########"]
    print(find_route(grid3))  # None