class MaxList:
    def __init__(self):
        self.data = []
        self.toistaseksi_isoin = []

    def append(self, number):
        self.data.append(number)
        if not self.toistaseksi_isoin:
            self.toistaseksi_isoin.append(number)
        else:
            self.toistaseksi_isoin.append(max(self.toistaseksi_isoin[-1], number))

    def max(self):
        # TODO
        return self.toistaseksi_isoin[-1]

if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max()) # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max()) # 8
