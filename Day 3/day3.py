with open("input.txt", "r") as file:
    datas = file.readlines()

def part1(data):
    size = len(datas[0])
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
    '''
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
    '''
    return (zero, one)

def part2():
    i = 0
    oxy = datas
    zero, one = part1(datas)
    length = len(zero)
    while i < length:
        temp1 = []
        #print("Zero:", zero[i], "| One:", one[i])
        for each in oxy:
            if (zero[i] > one[i]) and (each[i] == '0'):
                temp1.append(each.strip())
            elif (one[i] > zero[i]) and (each[i] == '1'):
                temp1.append(each.strip())
            elif (one[i] == zero[i]) and (each[i] == '1'):
                print("Here")
                temp1.append(each.strip())
        oxy = temp1
        if len(oxy) == 1:
            break
        zero, one = part1(oxy)
        i += 1

    co2 = datas
    zero, one = part1(datas)
    i = 0
    while i < length:
        temp = []
        for each in co2:
            if (zero[i] < one[i]) and (each[i] == '0'):
                temp.append(each.strip())
            elif (one[i] < zero[i]) and (each[i] == '1'):
                temp.append(each.strip())
            elif (one[i] == zero[i]) and (each[i] == '0'):
                temp.append(each.strip())
        co2 = temp
        if len(co2) == 1:
            break
        i += 1
        zero, one = part1(co2)

    print(oxy)
    print(co2)

part2()
