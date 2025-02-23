class RepeatList:
    def __init__(self):
        self.vanhat = set()
        self.joo_repeat = False

    def append(self, number):
        if number in self.vanhat:
            self.joo_repeat = True
        else:
            self.vanhat.add(number)

    def repeat(self):
        return self.joo_repeat

if __name__ == "__main__":
    numbers = RepeatList()

    print(numbers.repeat()) # False

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.repeat()) # False

    numbers.append(2)
    print(numbers.repeat()) # True

    numbers.append(5)
    print(numbers.repeat()) # True