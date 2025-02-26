def count_rooms(grid):
    rivit = len(grid)
    sar = len(grid[0])
    kayty = [[False] * sar for _ in range(rivit)]
    
    def checkkaa(x, y):
        if x < 0 or x >= rivit or y < 0 or y >= sar:
            return
        if grid[x][y] == '#' or kayty[x][y]:
            return
        
        kayty[x][y] = True
        
        checkkaa(x + 1, y)
        checkkaa(x - 1, y)
        checkkaa(x, y + 1)
        checkkaa(x, y - 1)

    room_count = 0
    for i in range(rivit):
        for j in range(sar):
            if grid[i][j] == '.' and not kayty[i][j]:
                checkkaa(i, j)
                room_count += 1

    return room_count


if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid)) # 4

    grid = ["########",
            "#......#",
            "#.####.#",
            "#......#",
            "########"]
    print(count_rooms(grid)) # 1

    grid = ["########",
            "######.#",
            "##.#####",
            "########",
            "########"]
    print(count_rooms(grid)) # 2
