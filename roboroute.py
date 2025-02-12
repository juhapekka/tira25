def analyze_route(grid):
    paikka = (0,0)
    suunta = (0, -1)
    for y, rivi in enumerate(grid):
        if 'R' in rivi:
            paikka = (rivi.index('R'), y)

    visited_griddi = [[(0, 0) for _ in range(len(r))] for r in grid]

    suunnat = { (0, 1): (-1, 0), 
               (-1, 0): (0, -1), 
               (0, -1): (1, 0), 
               (1, 0): (0, 1) }

    cc = 0
    while visited_griddi[paikka[1]][paikka[0]] != suunta:

        if visited_griddi[paikka[1]][paikka[0]] == (0, 0):
            cc += 1
            visited_griddi[paikka[1]][paikka[0]] = suunta

        newco = (paikka[0] + suunta[0], paikka[1] + suunta[1])

        if not (0 <= newco[0] < len(grid[0]) and 0 <= newco[1] < len(grid)):
            return  (cc, True) 

        if grid[newco[1]][newco[0]] == '#':
            suunta = suunnat[suunta]
            continue


        paikka = newco
        """
        row_as_list = list(grid[newco[1]])
        row_as_list[newco[0]] = 'X'
        grid[newco[1]] = ''.join(row_as_list)
        for row in grid:
            print(row)
        print("------")
        input()
        """
    return (cc, False)






if __name__ == "__main__":
    grid1 = [".#......",
             "..#.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid1)) # (14, True)

    grid2 = ["........",
             ".##.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid2)) # (12, False)
