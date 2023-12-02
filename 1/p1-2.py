sum = 0


def handleLine(line: str) -> int:
    numbersWords = {
        "zero": "0",
        "0": "0",
        "one": "1",
        "1": "1",
        "two": "2",
        "2": "2",
        "three": "3",
        "3": "3",
        "four": "4",
        "4": "4",
        "five": "5",
        "5": "5",
        "six": "6",
        "6": "6",
        "seven": "7",
        "7": "7",
        "eight": "8",
        "8": "8",
        "nine": "9",
        "9": "9"}

    numsFound = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[i:j] in numbersWords:
                numsFound.append(numbersWords[line[i:j]])
                break

    return int(numsFound[0] + numsFound[-1])


with open('p1input.txt', 'r') as f:
    for line in f:
        sum += handleLine(line)

print(sum)
