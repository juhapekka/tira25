class PermutationTracker:
    def __init__(self):
        self.ll = 0
        self.amo = {}
        self.numbat = 0
        self.duplikaatit = 0
        
        self.pienin = 600
        self.suurin = 0

    def append(self, number):
        self.ll += 1
        
        new_co = self.amo.get(number, 0) + 1
        self.amo[number] = new_co
        
        if new_co == 1:
            self.numbat += 1
        elif new_co == 2:
            self.duplikaatit += 1
        
        if number < self.pienin:
            self.pienin = number
        if number > self.suurin:
            self.suurin = number

    def check(self):
        # Ei duplikaatteja
        # numbat == ll
        # pienin == 1
        # suurin == ll
        if self.duplikaatit > 0:
            return False
        if self.numbat != self.ll:
            return False
        if self.pienin != 1:
            return False
        if self.suurin != self.ll:
            return False
        
        return True
    

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False