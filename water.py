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

def rulet(tila, O, V):
    rtilat = []
    v, o = tila

    if v < V: rtilat.append(((V, o), V - v))
    if o < O: rtilat.append(((v, O), O - o))
    if v > 0: rtilat.append(((0, o), v))
    if o > 0: rtilat.append(((v, 0), o))
    if v > 0 and o < O:
        kaada = min(v, O - o)
        rtilat.append(((v - kaada, o + kaada), kaada))
    if o > 0 and v < V:
        kaada = min(o, V - v)
        rtilat.append(((v + kaada, o - kaada), kaada))
    
    #print(rtilat)
    return rtilat
    
def min_amount_liianhidas(left_volume, right_volume, target):
    # TODO

    if target > left_volume:
        return -1

    tilat = []
    for v in range(left_volume + 1):
        for o in range(right_volume + 1):
            tilat.append((v, o))

    D = Dijkstra(tilat)

    for tila in tilat:
        for stila, w in rulet(tila, right_volume, left_volume):
            D.add_edge(tila, stila, w)

    d = D.find_distances((0, 0))

    rval = float('inf')
    for o in range(right_volume + 1):
        w = d.get((target, o), float('inf'))
        rval = min(rval, w)

    return rval if rval != float('inf') else -1

def min_amount(left_volume, right_volume, target):
    if target > left_volume:
        return -1

    d = {(0, 0): 0}
    jono = [(0, (0, 0))]
    rval = float('inf')

    while jono:
        w, tila = heapq.heappop(jono)

        if tila[0] == target:
            rval = min(rval, w)

        for stila, ww in rulet(tila, right_volume, left_volume):
            www = w + ww

            if www < d.get(stila, float('inf')):
                d[stila] = www
                heapq.heappush(jono, (www, stila))

    return rval if rval != float('inf') else -1



if __name__ == "__main__":
    print(min_amount(5, 4, 2)) # 22
    print(min_amount(4, 3, 2)) # 16
    print(min_amount(3, 3, 1)) # -1
    print(min_amount(1, 1, 10**9)) # -1
    print(min_amount(10, 9, 8)) # 46
    print(min_amount(123, 456, 42)) # 10530

    print(min_amount(11, 9, 10)) #136