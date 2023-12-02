def handleRound(round: str):
    limit = {"red": 12, "green": 13, "blue": 14}
    selection = round.split(", ")
    for s in selection:
        num, color = s.split(" ")
        if limit[color] < int(num):
            return False
    return True

def handleRounds(rounds: str):
    roundsArr = rounds.split(";")
    return all([handleRound(r.strip()) for r in roundsArr])


def handleLine(line: str):
    _, rounds = line.split(":")
    return handleRounds(rounds)

with open('input.txt', 'r') as f:
    res = 0
    for i, line in enumerate(f):
        if handleLine(line):
            res += (i + 1)
    print(res)
