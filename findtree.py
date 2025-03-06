class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_tree(grid):
    d = { '/' : -1, '|' :  0, '\\':  1, }
    rivit = len(grid)
    sars = len(grid[0]) if rivit > 0 else 0

    node_paikat = []
    for r in range(rivit):
        for s in range(sars):
            ch = grid[r][s]
            if ch.isdigit():
                node_paikat.append((r, s))

    def cmp_char(y, x, ch):
        if 0 <= y < rivit and 0 <= x < sars and grid[y][x] == ch:
            return True
        return False

    def tee_puu(lehti, coords):
        for i, k in d.items():
            if cmp_char(coords[0] + 1, coords[1] + k, i):
                for n in node_paikat:
                    if n[0] > coords[0] and (coords[0] - n[0] == (coords[1] - n[1]) * k or (k == 0 and coords[1] == n[1])):
                        uusi_lehti = Node(int(grid[n[0]][n[1]]))
                        lehti.children.append(uusi_lehti)
                        tee_puu(uusi_lehti, n)
                        break

        return

    lehti = Node(int(grid[node_paikat[0][0]][node_paikat[0][1]]))
    tee_puu(lehti, node_paikat[0])
    return lehti

if __name__ == "__main__":
    grid = [r"...........",
            r"...........",
            r"......5....",
            r"...../.\...",
            r"....3...\..",
            r"....|....1.",
            r"....2......"]
    tree = find_tree(grid)
    print(tree)
    # Node(5, [Node(3, [Node(2)]), Node(1)])

    grid = [r"....1.....",
            r".../.\....",
            r"..2...\...",
            r"..|....3..",
            r"..7.../|\.",
            r"./.\.4.5.6",
            r"8...9....."]
    tree = find_tree(grid)
    print(tree)
    # Node(1, [Node(2, [Node(7, [Node(8), Node(9)])]), Node(3, [Node(4), Node(5), Node(6)])])

    grid = [r"6"]
    tree = find_tree(grid)
    print(tree)
