lines = []

with open('input.txt', 'r') as f:
    lines = f.readlines()


def createMap(lines):
    networkMap = {}
    for line in lines:
        key, val = line.split("=")
        key = key.strip()
        val = val.strip()
        val = val.split(",")
        val = [v.strip() for v in val]
        val = (val[0][1:], val[1][:-1])
        networkMap[key] = val
    return networkMap


def findSolution(steps, lines, networkMap):
    res = 0
    curr = lines[2][:3]
    while curr != "ZZZ":
        for step in steps:
            if step == "R":
                curr = networkMap[curr][1]
            elif step == "L":
                curr = networkMap[curr][0]
            print(curr)
            res += 1
    return res


lines = [line.strip() for line in lines]
steps = lines[0]

networkMap = createMap(lines[2:])
print(findSolution(steps, lines, networkMap))
