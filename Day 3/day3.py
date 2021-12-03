with open("input.txt", "r") as file:
    data = file.readlines()

def part1():
    size = len(data[0])
    zero = list()
    one = list()
    for each in range(size-1):
        zero.append(0)
        one.append(0)
    for each in data:
        i = 0
        for char in each.strip():
            if char == '0':
                zero[i] += 1
            else:
                one[i] += 1
            i += 1
    i = 0
    gamma = ""
    epsilon = ""
    while i < len(zero):
        if zero[i] > one[i]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
        i += 1
    print(gamma)
    print(epsilon)

part1()
