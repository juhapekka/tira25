import collections

class FlipList:
    def __init__(self):
        # TODO
        self.dadad = collections.deque()
        self.negat = False

    def __repr__(self):
        # TODO
        if self.negat:
            e = list(reversed(self.dadad))
        else:
            e = list(self.dadad)

        kamat = ", ".join(map(str, e))
        return f"[{kamat}]"

    def add_first(self, x):
        # TODO

        if self.negat:
            self.dadad.append(x)
        else:
            self.dadad.appendleft(x)

    def add_last(self, x):
        # TODO
        if self.negat:
            self.dadad.appendleft(x)
        else:
            self.dadad.append(x)

    def flip(self):
        # TODO
        self.negat = not self.negat

if __name__ == "__main__":
    numbers = FlipList()

    numbers.add_last(1)
    numbers.add_last(2)
    numbers.add_last(3)
    print(numbers) # [1, 2, 3]

    numbers.add_first(4)
    print(numbers) # [4, 1, 2, 3]

    numbers.flip()
    print(numbers) # [3, 2, 1, 4]

    numbers.add_last(5)
    print(numbers) # [3, 2, 1, 4, 5]