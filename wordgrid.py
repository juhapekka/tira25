class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        self.rivit = len(grid)
        self.jonot = len(grid[0])
    
    def gridissa(self, x, y):
        return 0 <= x < self.jonot and 0 <= y < self.rivit

    def check_direction(self, xx, yy, xadd, yadd, word):
        positions = []
        kirjaimet = []
        x, y = xx, yy
        for i in range(len(word)):
            if not self.gridissa(x, y):
                return None
            kirjaimet.append(self.grid[y][x])
            positions.append((x, y))
            x += xadd
            y += yadd

        found = ''.join(kirjaimet)

        # sana voi tulla myös takaperin.
        if found == word or found == word[::-1]:
            return tuple(positions)
        return None
        
    def count(self, word):
        seen = set()
        cc = 0
        suunnat = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                for xadd, yadd in suunnat:
                    tulos = self.check_direction(x, y, xadd, yadd, word)
                    if tulos:

                        avain = frozenset(tulos)
                        if avain not in seen:
                            cc += 1
                            seen.add(avain)
        return cc

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0    