class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        # TODO
        if not self.root:
            self.root = Node(value)
            self.max_depth += 1
            return

        node = self.root
        syvyys = 0
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    if self.max_depth < syvyys + 1:
                        self.max_depth = syvyys + 1
                    return
                node = node.left
                syvyys += 1
            else:
                if not node.right:
                    node.right = Node(value)
                    if self.max_depth < syvyys + 1:
                        self.max_depth = syvyys + 1
                    return
                node = node.right
                syvyys += 1

    def height(self):
        return self.max_depth

if __name__ == "__main__":
    numbers = TreeSet()
    print(numbers.height()) # -1
    numbers.add(2)
    print(numbers.height()) # 0
    numbers.add(1)
    print(numbers.height()) # 1
    numbers.add(3)
    print(numbers.height()) # 1
    numbers.add(4)
    print(numbers.height()) # 2