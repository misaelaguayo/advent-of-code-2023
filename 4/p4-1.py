def countMatches(card1, card2):
    res = 0
    seen = set(card1)
    for card in card2:
        if card in seen:
            res += 1
    return res

def calculateScore(count):
    if count <= 0:
        return 0
    return 2 ** (count - 1)

def makeCard(row):
    _, newRow = row.split(":")
    card1, card2 = newRow.split("|")
    card1 = list(filter(lambda x: x != "", card1.strip().split(" ")))
    card2 = list(filter(lambda x: x != "", card2.strip().split(" ")))
    return [int(c) for c in card1], [int(c) for c in card2]

cards = []
with open ('input.txt', 'r') as f:
    for line in f:
        cards.append(makeCard(line))

res = 0
for winning, ticket in cards:
    matches = countMatches(winning, ticket)
    res += calculateScore(matches)

print(res)
