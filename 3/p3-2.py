def makeGrid():
    grid = []
    with open ('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            grid.append([c for c in line])
    return grid

def hasSymbolAround(grid, r, c):
    numbers = "0123456789"
    offset = [0, 1, -1]
    rows = len(grid)
    columns = len(grid[0])

    for i in offset:
        for j in offset:
            if r + i >= 0 and r + i < rows and c + j >= 0 and c + j < columns:
                if grid[r+i][c+j] not in numbers and grid[r+i][c+j] != ".":
                    return True
    return False

def findSchems(grid, r):
    res = []
    numbers = "0123456789"
    currNum = ""
    hasSymbol = False
    string = grid[r]
    for c in range(len(string)):
        if string[c] not in numbers:
            if currNum:
                res.append((currNum, hasSymbol))
            currNum = ""
            hasSymbol = False
        else:
            currNum += string[c]
            hasSymbol = hasSymbol or hasSymbolAround(grid, r, c)
    if currNum:
        res.append((currNum, hasSymbol))
    return res

def main():
    grid = makeGrid()
    res = 0

    for row in range(len(grid)):
        nums = findSchems(grid, row)
        schems = list(filter(lambda x: x[1], nums))
        res += sum([int(schem[0]) for schem in schems])

    return res

