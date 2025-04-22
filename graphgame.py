#mallivastaus..
class GraphGame2:
    def __init__(self, n):
        self.graph = {node: [] for node in range(1, n + 1)}
 
    def add_link(self, a, b):
        self.graph[a].append(b)
 
    def can_win(self, x, results={}):
        if x not in results:
            result = False
            for y in self.graph[x]:
                if not self.can_win(y):
                    result = True
            results[x] = result
        return results[x]
 
    def winning(self, x):
        return self.can_win(x)

class GraphGame:
    def __init__(self, n):
        self.n = n
        self.noodit = list(range(1, n + 1))
        self.graph = {i: [] for i in self.noodit}


    def add_link(self, a, b):
        self.graph[a].append(b)


    def winning(self, x):
        naapurit = self.graph.get(x, [])

        for v in naapurit:
            if not self.winning(v):
                return True

        return False


if __name__ == "__main__":
    """
    game = GraphGame(6)

    game.add_link(3, 4)
    game.add_link(1, 4)
    game.add_link(4, 5)

    print(game.winning(3)) # False
    print(game.winning(1)) # False

    game.add_link(3, 1)
    game.add_link(4, 6)
    game.add_link(6, 5)

    print(game.winning(3)) # True
    print(game.winning(1)) # False
    print(game.winning(2)) # False
    """

"""    
Viikon 13 "verkkopeli" tehtävän mallivastauksessa näyttäisi olevan virhe
liittyen pythonin mutablen käyttöön. Esimerkkiratkaisu ei toimi oikein jos
verkkoa muutetaan. Alla esimerkki ongelmasta:
"""
bugi = GraphGame2(3)
bugi.add_link(1, 2)
testinoodi = 1

# verkko: 1 -> 2
ennen_tulos = bugi.winning(testinoodi)

bugi.add_link(2, 3)
# verkko: 1 -> 2 -> 3
jalkeen_tulos = bugi.winning(testinoodi)

if jalkeen_tulos == True and ennen_tulos == True:
    print("metodi palautti väärän tuloksen")
elif jalkeen_tulos == False:
    print("bugi korjattu")
else:
    print("jotain muuta")
