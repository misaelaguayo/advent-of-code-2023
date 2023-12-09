lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

def calculateNextNumber(numbers):
    if all([number == 0 for number in numbers]):
        return 0
    newNumbers = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]
    return numbers[-1] + calculateNextNumber(newNumbers)

def solution(lines):
    lines = [line.strip() for line in lines]
    lines = [list(map(int, line.strip().split(" "))) for line in lines]
    res = sum([calculateNextNumber(line) for line in lines])
    return res

print(solution(lines))
