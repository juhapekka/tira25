class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1
 
class TreeSet:
    def __init__(self):
        self.root = None
 
    def add(self, value):
        # TODO
        if not self.root:
            self.root = Node(value)
            return
 
        node = self.root
        while True:
            if node.value == value:
                node.count += 1
                return
            
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    return
                
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

    def _eti(self, node, value):

        while node:
            if node.value == value:
                return node.count
            elif node.value > value:
                node = node.left
            else:
                node = node.right

        return 0

    def __contains__(self, value):
        # TODO
        return self._eti(self.root, value) > 0


    def __repr__(self):
        # TODO
        items = []

        def kelaa(node, items):
            if node is None:
                return

            kelaa(node.left, items)
            items += [node.value] * node.count
            kelaa(node.right, items)

        kelaa(self.root, items)
        return str(items)

    def count(self, value):
        # TODO
        return self._eti(self.root, value)

if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(4)
    numbers.add(1)
    numbers.add(2)
    numbers.add(1)

    print(numbers) # [1, 1, 2, 4]

    print(1 in numbers) # True
    print(2 in numbers) # True
    print(3 in numbers) # False
    print(4 in numbers) # True

    print(numbers.count(1)) # 2
    print(numbers.count(2)) # 1
    print(numbers.count(3)) # 0
    print(numbers.count(4)) # 1

    print("-------")

    numbers = TreeSet()
    numbers.add(1)
    numbers.count(1)
    print(numbers)
    numbers.add(3)
    numbers.count(1)
    print(numbers)
    numbers.add(2)
    numbers.count(3)
    print(numbers)
