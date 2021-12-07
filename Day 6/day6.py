with open("input.txt", "r") as file:
    data = file.readlines()

def part1(days):
    state = data[0].split(",")
    while days != 0:
        print(days)
        temp = list()
        for each in state:
            if int(each) > 0:
                temp.append(int(each) - 1)
            else:
                temp.append(6)
                temp.append(8)
        state = temp
        days -= 1
    return len(state)

def part2(days):
    fish_map = mapcreator(data[0].split(','))
    for _ in range(days):
        temp_fish_map= dict()
        for each in range(9):
            temp_fish_map[each] = 0
        for timer, fishes in fish_map.items():
            timer -= 1
            if int(timer) < 0:
                temp_fish_map[8] = fishes
                temp_fish_map[6] += fishes
            else:
                temp_fish_map[int(timer)] += fishes
        fish_map = temp_fish_map
    return sum(fish_map.values())


def mapcreator(fishies):
    retval = dict()
    for each in range(9):
        retval[each] = 0
    for each in fishies:
        retval[int(each)] += 1
    return retval


#print(part1(80))
print(part2(256))
