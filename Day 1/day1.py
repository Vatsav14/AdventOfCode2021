# Part 1
with open("input.txt", "r") as file:
    data = file.readlines()
def part1():
    increasing = 0
    prev = data[0]
    for each in data:
        if each > prev:
            increasing += 1
        prev = each
    return increasing

def part2():
    increasing = 0
    prev_sum = int(data[0]) + int(data[1]) + int(data[2])
    i = 1
    for each in data[1:-2]:
        current = int(data[i]) + int(data[i+1]) + int(data[i+2])
        if current > prev_sum:
            increasing += 1
        prev_sum = current
        i+=1
    return increasing

increasing = part2()
print(increasing)
