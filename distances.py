class DistanceTracker:
    def __init__(self):
        self.d = {}
        self.amo = 0

    def append(self, number):
        if number not in self.d.keys():
            self.d[number] = {'amo': 0, 'pos': 0, 'sum': 0}

        l = self.d[number]

#        print(l)

        sumsum = l['sum']
        if l['amo'] > 0:
            sumsum += (l['amo'] * self.amo) - l['pos']

        self.d[number] = {'amo': l['amo'] + 1, 'pos': l['pos'] + self.amo, 'sum': sumsum}
        self.amo += 1



    def sum(self, number):
        if number not in self.d.keys():
            return 0
        
#        print (number)

        return self.d[number]['sum']
               
 

        

if __name__ == "__main__":
    tracker = DistanceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    tracker.append(3)
    tracker.append(1)
    tracker.append(2)
    tracker.append(1)

    print(tracker.sum(1)) # 24
    print(tracker.sum(2)) # 5
    print(tracker.sum(3)) # 1

    tracker.append(1)
    tracker.append(2)
    tracker.append(3)

    print(tracker.sum(1)) # 42
    print(tracker.sum(2)) # 16
    print(tracker.sum(3)) # 14

    tracker = DistanceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(1)
        total += tracker.sum(1)


    print(total) # 4166749999583325000