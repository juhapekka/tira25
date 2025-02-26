class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_levels(node):
    levellit = []
    """
    def tayta_levellit(node, depth):
        if depth == 0:
            return 1
        else:
            leaves = 0
            for child in node.children:
                leaves += count_nodes(child, depth - 1)
            return leaves
    """

    def tayta_levellit(node, depth):
        if len(levellit) <= depth:
            levellit.append([])

        levellit[depth].append(node.value)
        for child in node.children:
            tayta_levellit(child, depth + 1)

    tayta_levellit(node, 0)
    for l in range(len(levellit)):
        levellit[l] = sorted(levellit[l])
    return levellit


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_levels(tree1)) # [[1], [2, 4, 5], [3, 6, 7]]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_levels(tree2)) # [[1], [2], [3], [4]]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_levels(tree3)) # [[1], [2, 3, 4]]