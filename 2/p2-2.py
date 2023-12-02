def handleRound(round: str):
    minimum = {"red": 0, "green": 0, "blue": 0}
    selection = round.split(", ")
    for s in selection:
        num, color = s.split(" ")
        minimum[color] = int(num)
    return minimum

def handleRounds(rounds: str):
    roundsArr = rounds.split(";")
    minRed = minGreen = minBlue = 0
    for r in roundsArr:
        res = handleRound(r.strip())
        minRed = max(minRed, res["red"])
        minGreen = max(minGreen, res["green"])
        minBlue = max(minBlue, res["blue"])
    return minRed * minGreen * minBlue


def handleLine(line: str):
    _, rounds = line.split(":")
    return handleRounds(rounds)

with open('input.txt', 'r') as f:
    res = 0
    for line in f:
        res += handleLine(line)
    print(res)

