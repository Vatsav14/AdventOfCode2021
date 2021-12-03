with open("input.txt", "r") as file:
    data = file.readlines()

def part1():
    hor = 0
    depth = 0
    for each in data:
        line = each.split()
        if line[0] == "forward":
            hor += int(line[1])
        elif line[0] == "down":
            depth += int(line[1])
        else:
            depth -= int(line[1])
    print("Horizontal:", hor)
    print("Depth:", depth)

def part2():
    hor = 0
    depth = 0
    aim = 0
    for each in data:
        line = each.split()
        if line[0] == "forward":
            hor += int(line[1])
            depth += aim * int(line[1])
        elif line[0] == "down":
            aim += int(line[1])
        else:
            aim -= int(line[1])
    print("Horizontal:", hor)
    print("Depth:", depth)

part2()
