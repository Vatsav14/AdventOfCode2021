with open("input.txt", "r") as file:
    data = [x.split() for x in file.readlines()]

def calculateScore(brac):
    stack = []
    for each in brac:
        if each is '[' or each is '(' or each is '{' or each is '<':
            stack.append(each)
        else:
            if len(stack) == 0:
                return each
            if each is ']' and stack[-1] is not '[':
                return each
            if each is ')' and stack[-1] is not '(':
                return each
            if each is '}' and stack[-1] is not '{':
                return each
            if each is '>' and stack[-1] is not '<':
                return each
            stack.pop()
    return None

def getValue(brac):
    if brac is ')':
        return 3
    if brac is ']':
        return 57
    if brac is '}':
        return 1197
    if brac is '>':
        return 25137
    return 0

def newGetValue(brac):
    if brac is '(':
        return 1
    if brac is '[':
        return 2
    if brac is '{':
        return 3
    if brac is '<':
        return 4
    return 0

def part1():
    total = 0
    for each in data:
        total += getValue(calculateScore(each[0]))
    return total

def complete(brac):
    stack = []
    completion = []
    for each in brac:
        if each is '[' or each is '(' or each is '{' or each is '<':
            stack.append(each)
        else:
            if len(stack) == 0:
                return None
            if each is ']' and stack[-1] is not '[':
                return None
            if each is ')' and stack[-1] is not '(':
                return None
            if each is '}' and stack[-1] is not '{':
                return None
            if each is '>' and stack[-1] is not '<':
                return None
            stack.pop()
    return stack

def calculateCompl(complete):
    score = 0
    while(len(complete) != 0):
        score = ((5 * score) + newGetValue(complete.pop()))
    return score

def part2():
    scoreList = []
    for each in data:
        temp = complete(each[0])
        if temp is not None:
            scoreList.append(calculateCompl(temp))
    print(sorted(scoreList)[len(scoreList)//2])

part2()
