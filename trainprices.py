
# materiaaleista https://tira.mooc.fi/kevat-2025/osa14/#floyd-warshall-algoritmi
class FloydWarshall:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        for a in self.nodes:
            for b in self.nodes:
                distance = 0 if a == b else float("inf")
                self.graph[(a, b)] = distance

    def add_edge(self, a, b, w):
        self.graph[(a, b)] = min(self.graph[(a, b)], w)

    def find_distances(self):
        distances = self.graph.copy()

        for k in self.nodes:
            for a in self.nodes:
                for b in self.nodes:
                    distance = min(distances[(a, b)],
                                   distances[(a, k)] +
                                   distances[(k, b)])
                    distances[(a, b)] = distance

        return distances


class TrainPrices:
    def __init__(self):
        self.kaupunnit = []
        self.junat = []

    def add_city(self, name):
        self.kaupunnit.append(name)


    def add_train(self, city1, city2, price):
        self.junat.append((city1, city2, price))

    def find_prices(self):
        sortedkaupunnit = sorted(self.kaupunnit)
        rval = [[None] + sortedkaupunnit]
        fw = FloydWarshall(sortedkaupunnit)

        for city1, city2, price in self.junat:
            fw.add_edge(city1, city2, price)
            fw.add_edge(city2, city1, price)

        lyhimmat = fw.find_distances()

        for lahto in sortedkaupunnit:
            rivi = [lahto]
            #print("---")
            for maali in sortedkaupunnit:
                d = lyhimmat.get((lahto, maali), float('inf'))
                p = d if d != float('inf') else -1
                rivi.append(p)
                #print(rivi)
            rval.append(rivi)

        return rval


if __name__ == "__main__":
    prices = TrainPrices()

    prices.add_city("Helsinki")
    prices.add_city("Turku")
    prices.add_city("Tampere")
    prices.add_city("Oulu")

    prices.add_train("Helsinki", "Tampere", 20)
    prices.add_train("Helsinki", "Turku", 10)
    prices.add_train("Tampere", "Turku", 50)

    print(prices.find_prices())

    # metodin haluttu tulos:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]
