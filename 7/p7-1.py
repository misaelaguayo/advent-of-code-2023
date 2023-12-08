from collections import Counter
import functools
lines = []

with open('input.txt', 'r') as f:
    lines = f.readlines()

def isFiveOfKind(hand, ctr):
    return len(set(hand)) == 1 and 5 in ctr.values()

def isFourOfKind(hand, ctr):
    return len(set(hand)) == 2 and 4 in ctr.values()

def isFullHouse(hand, ctr):
    return len(set(hand)) == 2 and 3 in ctr.values()

def isThreeOfKind(hand, ctr):
    return len(set(hand)) == 3 and 3 in ctr.values()

def isTwoPair(hand, ctr):
    return len(set(hand)) == 3 and 2 in ctr.values()

def isOnePair(hand, ctr):
    return len(set(hand)) == 4 and 2 in ctr.values()

def isHighCard(hand, ctr):
    return len(set(hand)) == 5 and 1 in ctr.values()

def isSameScore(hand1, hand2):
    ctr1 = Counter(hand1)
    ctr2 = Counter(hand2)
    return isFiveOfKind(hand1, ctr1) and isFiveOfKind(hand2, ctr2) or \
        isFourOfKind(hand1, ctr1) and isFourOfKind(hand2, ctr2) or \
        isFullHouse(hand1, ctr1) and isFullHouse(hand2, ctr2) or \
        isThreeOfKind(hand1, ctr1) and isThreeOfKind(hand2, ctr2) or \
        isTwoPair(hand1, ctr1) and isTwoPair(hand2, ctr2) or \
        isOnePair(hand1, ctr1) and isOnePair(hand2, ctr2) or \
        isHighCard(hand1, ctr1) and isHighCard(hand2, ctr2)

def comparator(item1, item2):
    hand1 = item1[0]
    hand2 = item2[0]
    ctr1 = Counter(hand1)
    ctr2 = Counter(hand2)
    mapping = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    if isSameScore(hand1, hand2):
        for i in range(5):
            if mapping[hand1[i]] > mapping[hand2[i]]:
                return 1
            elif mapping[hand1[i]] < mapping[hand2[i]]:
                return -1
        return 0
    if isFiveOfKind(hand1, ctr1):
        return 1
    if isFiveOfKind(hand2, ctr2):
        return -1
    if isFourOfKind(hand1, ctr1):
        return 1
    if isFourOfKind(hand2, ctr2):
        return -1
    if isFullHouse(hand1, ctr1):
        return 1
    if isFullHouse(hand2, ctr2):
        return -1
    if isThreeOfKind(hand1, ctr1):
        return 1
    if isThreeOfKind(hand2, ctr2):
        return -1
    if isTwoPair(hand1, ctr1):
        return 1
    if isTwoPair(hand2, ctr2):
        return -1
    if isOnePair(hand1, ctr1):
        return 1
    if isOnePair(hand2, ctr2):
        return -1
    if isHighCard(hand1, ctr1):
        return 1
    if isHighCard(hand2, ctr2):
        return -1

def calculateResult(cards):
    res = 0
    for i in range(len(cards)):
        res += (i+1) * int(cards[i][1])
    return res

cards = [line.strip().split(' ') for line in lines]
cards.sort(key=functools.cmp_to_key(comparator))
print(calculateResult(cards))
