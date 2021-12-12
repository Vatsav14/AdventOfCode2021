with open("input.txt", "r") as file:
    data = [x.split() for x in file.readlines()]

def part1():
    count = 0
    for each in data:
        consider = each[-4:]
        for every in consider:
            if len(every) == 2 or len(every) == 3 or len(every) == 4 or len(every) == 7:
                count += 1
    return count
                

print(part1())
