#https://tira.mooc.fi/kevat-2025/osa8/#lyhimm%C3%A4t-polut-ja-et%C3%A4isyydet
class ShortestPaths:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def find_path(self, start_node, end_node):
        distances = {}
        previous = {}

        queue = [start_node]
        distances[start_node] = 0
        previous[start_node] = None

        for node in queue:
            distance = distances[node]
            for next_node in self.graph[node]:
                if next_node not in distances:
                    queue.append(next_node)
                    distances[next_node] = distance + 1
                    previous[next_node] = node

        if end_node not in distances:
            return None

        node = end_node
        path = []
        while node:
            path.append(node)
            node = previous[node]

        path.reverse()
        return path

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def keraa_lehdet(node, val):
    val.add(node.value)
    for c in node.children:
        keraa_lehdet(c, val)

def tee_edget(node, sp_obj, parent=None):
    if parent is not None:
        sp_obj.add_edge(parent.value, node.value)

    for c in node.children:
        tee_edget(c, sp_obj, node)

def find_path(node, a, b):
    # TODO
    lehdet = set()
    keraa_lehdet(node, lehdet)

    if a not in lehdet or b not in lehdet:
        return None #ei polkua

    sp = ShortestPaths(lehdet)
    tee_edget(node, sp)
    path = sp.find_path(a, b)
    return path





if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_path(tree1, 3, 2)) # [3, 4, 1, 2]
    print(find_path(tree1, 1, 7)) # [1, 4, 7]
    print(find_path(tree1, 5, 5)) # [5]
    print(find_path(tree1, 7, 3)) # [7, 4, 3]
    print(find_path(tree1, 4, 8)) # None

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_path(tree2, 1, 4)) # [1, 2, 3, 4]
    print(find_path(tree2, 4, 1)) # [4, 3, 2, 1]
    print(find_path(tree2, 2, 3)) # [2, 3]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_path(tree3, 2, 3)) # [2, 1, 3]
    print(find_path(tree3, 1, 2)) # [1, 2]
    print(find_path(tree3, 5, 5)) # None