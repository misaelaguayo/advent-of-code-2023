def countMatches(card1, card2):
    res = 0
    seen = set(card1)
    for card in card2:
        if card in seen:
            res += 1
    return res

def makeCard(row):
    _, newRow = row.split(":")
    card1, card2 = newRow.split("|")
    card1 = list(filter(lambda x: x != "", card1.strip().split(" ")))
    card2 = list(filter(lambda x: x != "", card2.strip().split(" ")))
    return [int(c) for c in card1], [int(c) for c in card2]

cards = []
cardCount = 0
with open ('input.txt', 'r') as f:
    for line in f:
        cardCount += 1
        cards.append(makeCard(line))

cardMatches = []
for winning, ticket in cards:
    matches = countMatches(winning, ticket)
    cardMatches.append(matches)

iterations = [1] * cardCount

for i in range(len(iterations)):
    matches = cardMatches[i]
    for j in range(1, matches + 1):
        if i + j < len(iterations):
            iterations[i+j] += iterations[i]

print(sum(iterations))
