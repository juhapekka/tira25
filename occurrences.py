class OccurrenceTracker:
    def __init__(self):
        self.dadat = {}

    def append(self, number):
        if number not in self.dadat.keys():
            self.dadat[number] = 1
        else:
            self.dadat[number] += 1

    def count(self):
        return len(list(set(self.dadat.values())))

if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3