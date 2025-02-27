def count_patterns(grid):
    korkeus = len(grid)
    leveys = len(grid[0])

    suunnat = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    nahty = [[False] * leveys for _ in range(korkeus)]

    def leveyshaku(start_y, start_x):
        queue = [(start_y, start_x)]
        nahty[start_y][start_x] = True
        visited = [(start_y, start_x)]

        for y, x in queue:
            for dy, dx in suunnat:
                ny, nx = y + dy, x + dx
                if 0 <= ny < korkeus and 0 <= nx < leveys:
                    if not nahty[ny][nx] and grid[ny][nx] == '*':
                        nahty[ny][nx] = True
                        queue.append((ny, nx))
                        visited.append((ny, nx))

        return visited

    patterns = set()

    for y in range(korkeus):
        for x in range(leveys):
            if grid[y][x] == '*' and not nahty[y][x]:
                cc = leveyshaku(y, x)

                # kuvion paikka
                min_y = min(pt[0] for pt in cc)
                max_y = max(pt[0] for pt in cc)
                min_x = min(pt[1] for pt in cc)
                max_x = max(pt[1] for pt in cc)

                boxi = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

                for (cy, cx) in cc:
                    by = cy - min_y
                    bx = cx - min_x
                    boxi[by][bx] = '*'

                # tuple settiä varten
                pattern = tuple("".join(row) for row in boxi)
                patterns.add(pattern)

    return len(patterns)


if __name__ == "__main__":
    grid1 = ["..*..*..",
             "**.....*",
             ".....**.",
             "...*....",
             ".**....*"]
    print(count_patterns(grid1))  # 2

    grid2 = ["....*..*",
             "*.......",
             "......*.",
             "..*.....",
             "......*."]
    print(count_patterns(grid2))  # 1

    grid3 = ["***.*.**",
             ".*..*..*",
             ".*.***..",
             ".......*",
             "......**"]
    print(count_patterns(grid3))  # 4

    grid4 = ["***.***.",
             "..*...*.",
             "**..**..",
             "..*...*.",
             "**..**.."]
    print(count_patterns(grid4))  # 1