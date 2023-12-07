def makeGrid():
    grid = []
    with open ('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            grid.append([c for c in line])
    return grid

def visitNumber(grid, r, c, seen):
    numbers = "0123456789"
    seen[r][c] = True
    left, right = c, c

    while left >= 0 and grid[r][left] in numbers:
        seen[r][left] = True
        left -= 1
    while right < len(grid[0]) and grid[r][right] in numbers:
        seen[r][right] = True
        right += 1
    return int("".join(grid[r][left+1:right]))

def visit(grid, r, c):
    numbers = "0123456789"
    seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    seen[r][c] = True

    moves = [1, 0, -1]
    nums = []
    for x in moves:
        for y in moves:
            if r + x >= 0 and r + x < len(grid) and c + y >= 0 and c + y < len(grid[0]) and not seen[r+x][c+y] and grid[r+x][c+y] in numbers:
                nums.append(visitNumber(grid, r+x, c+y, seen))

    return nums

def main():
    grid = makeGrid()
    r, c = len(grid), len(grid[0])
    res = 0
    for row in range(r):
        for column in range(c):
            if grid[row][column] == "*":
                v = visit(grid, row, column)
                if len(v) == 2:
                    res += v[0] * v[1]
    return res

print(main())
