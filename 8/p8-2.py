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


lines = [line.strip() for line in lines]
steps = lines[0]
networkMap = createMap(lines[2:])


def findSolution(steps, networkMap, keysEndingWithA):
    res = 0

    while any([key[-1] != "Z" for key in keysEndingWithA]):
        step = 1 if steps[res % len(steps)] == "R" else 0
        keysEndingWithA = [networkMap[key][step] for key in keysEndingWithA]
        res += 1
    return res


keysEndingWithA = [key for key in networkMap.keys() if key[-1] == "A"]
print(findSolution(steps, networkMap, [keysEndingWithA[0]]))
print(findSolution(steps, networkMap, [keysEndingWithA[1]]))
print(findSolution(steps, networkMap, [keysEndingWithA[2]]))
print(findSolution(steps, networkMap, [keysEndingWithA[3]]))
print(findSolution(steps, networkMap, [keysEndingWithA[4]]))
print(findSolution(steps, networkMap, [keysEndingWithA[5]]))
