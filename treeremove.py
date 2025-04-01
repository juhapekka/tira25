class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if node.value == value:
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

    def remove(self, value):
        # TODO
        node = self.root
        prevnode = None
        while True:
            if node.value == value:
                break
            if node.value > value:
                vasen = True
                if not node.left:
                    return
                prevnode = node
                node = node.left
            else:
                vasen = False
                
                if not node.right:
                    return
                prevnode = node
                node = node.right

        #print(f"founded {node.value}")

        # Ei ole lapsia
        if node.left is None and node.right is None:
            if prevnode is None:
                self.root = None
            elif vasen:
                prevnode.left = None
            else:
                prevnode.right = None

        # Yksi lapsi oikealla
        elif node.left is None:
            if prevnode is None: # juuri
                self.root = node.right
            elif vasen:
                prevnode.left = node.right
            else:
                prevnode.right = node.right

        # Yksi lapsi vasemmalla
        elif node.right is None:
            if prevnode is None: # juuri
                self.root = node.left
            elif vasen:
                prevnode.left = node.left
            else:
                prevnode.right = node.left
        
        # kaksi lasta
        else:
            seuraava_parentri = node
            seuraava = node.right
            while seuraava.left is not None:
                seuraava_parentri = seuraava
                seuraava = seuraava.left

            node.value = seuraava.value

            if seuraava_parentri == node:
                seuraava_parentri.right = seuraava.right
            else:
                seuraava_parentri.left = seuraava.right

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)

if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(3)
    numbers.add(2)
    numbers.add(5)
    numbers.add(7)
    print(numbers) # [2, 3, 5, 7]
    
    numbers.remove(3)
    print(numbers) # [2, 5, 7]

    numbers.remove(7)
    print(numbers) # [2, 5]

    numbers.remove(2)
    print(numbers) # [5]

    numbers.remove(5)
    print(numbers) # []