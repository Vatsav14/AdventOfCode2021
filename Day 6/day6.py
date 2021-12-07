with open("input.txt", "r") as file:
    data = file.readlines()

def part1(days):
    state = data[0].split(",")
    print(state)
    while days != 0:
        temp = list()
        extras = 0
        for each in state:
            if int(each) > 0:
                temp.append(int(each) - 1)
            else:
                temp.append(6)
                extras += 1
        for each in range(extras):
            temp.append(8)
        state = temp
        days -= 1
    return len(state)

print(part1(80))
