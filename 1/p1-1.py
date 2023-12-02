sum = 0


def handleLine(line: str) -> int:
    numbers = "0123456789"
    numsFound = []
    for c in line:
        if c in numbers:
            numsFound.append(c)

    return int(numsFound[0] + numsFound[-1])


with open('p1input.txt', 'r') as f:
    for line in f:
        sum += handleLine(line)

print(sum)
