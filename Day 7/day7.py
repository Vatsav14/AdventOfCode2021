with open("input.txt", "r") as file:
    data = [int(x) for x in file.read().split(",")]

def part1():
    minim = min(data)
    maxim = max(data) + 1
    least_abs = 10000000000000000
    pos = 100000000000000000000
    for each in range(minim, maxim):
        abs_val = 0
        for value in data:
            abs_val += abs(value - each)
        if abs_val < least_abs:
            least_abs = abs_val
            pos = each
    return (pos, least_abs)

def part2():
    minim = min(data)
    maxim = max(data) + 1
    least_abs = 10000000000000000
    pos = 100000000000000000000
    for each in range(minim, maxim):
        abs_val = 0
        for value in data:
            # Just use formula for sum upto N natural numbers
            abs_val += (abs(value - each) * (abs(value - each) + 1) / 2)
        if abs_val < least_abs:
            least_abs = abs_val
            pos = each
    return (pos, least_abs)


print(part1())
