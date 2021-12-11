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
            print('ending')
            if len(stack) == 0:
                completion.append('blank')
            if each is ']' and stack[-1] is not '[':
                completion.append(']')
            if each is ')' and stack[-1] is not '(':
                completion.append(')')
            if each is '}' and stack[-1] is not '{':
                completion.append('}')
            if each is '>' and stack[-1] is not '<':
                completion.append('>')
            stack.pop()
    return completion

def part2():
    for each in data:
        print(complete(each[0]))

part2()
