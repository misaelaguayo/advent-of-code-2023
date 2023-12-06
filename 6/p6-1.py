def products(arr):
    res = 1
    for a in arr:
        res *= a
    return res
lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
lines = [line.split(":")[1:][0].strip() for line in lines]
lines = [line.split(' ') for line in lines]
lines = [list(filter(lambda x: x, line)) for line in lines]

times, distances = lines
times = [int(t) for t in times]
distances = [int(d) for d in distances]

res = []
for t, time in enumerate(times):
    curr = 0
    for speed in range(time + 1):
        currDistance = speed * (time - speed)
        if currDistance > distances[t]:
            curr += 1
    res.append(curr)

res = products(res)
print(res)
