with open("input.txt", "r") as file:
    data = file.readlines()

insertions = data[0].split(',')


def win():
    boardn = 0
    for each in boards:
        if each[0][0] == '.' and each[0][1] == '.' and each[0][2] == '.' and each[0][3] == '.' and each[0][4] == '.':
            return (1, boardn)
        elif each[1][0] == '.' and each[1][1] == '.' and each[1][2] == '.' and each[1][3] == '.' and each[1][4] == '.':
            return (1, boardn)
        elif each[2][0] == '.' and each[2][1] == '.' and each[2][2] == '.' and each[2][3] == '.' and each[2][4] == '.':
            return (1, boardn)
        elif each[3][0] == '.' and each[3][1] == '.' and each[3][2] == '.' and each[3][3] == '.' and each[3][4] == '.':
            return (1, boardn)
        elif each[4][0] == '.' and each[4][1] == '.' and each[4][2] == '.' and each[4][3] == '.' and each[4][4] == '.':
            return (1, boardn)
        boardn += 1

        if each[0][0] == '.' and each[1][0] == '.' and each[2][0] == '.' and each[3][0] == '.' and each[4][0] == '.':
            return (1, boardn)
        elif each[0][1] == '.' and each[1][1] == '.' and each[2][1] == '.' and each[3][1] == '.' and each[4][1] == '.':
            return (1, boardn)
        elif each[0][2] == '.' and each[1][2] == '.' and each[2][2] == '.' and each[3][2] == '.' and each[4][2] == '.':
            return (1, boardn)
        elif each[0][3] == '.' and each[1][3] == '.' and each[2][3] == '.' and each[3][3] == '.' and each[4][3] == '.':
            return (1, boardn)
        elif each[0][4] == '.' and each[1][4] == '.' and each[2][4] == '.' and each[3][4] == '.' and each[4][4] == '.':
            return (1, boardn)
    return (0, boardn)

boards = list()
i = 2
while i < len(data):
    temp = list()
    temp.append(data[i].split())
    temp.append(data[i+1].split())
    temp.append(data[i+2].split())
    temp.append(data[i+3].split())
    temp.append(data[i+4].split())
    boards.append(temp)
    i += 6

def main():
    for each in insertions:
        for every in boards:
            for eachevery in every:
                i = 0
                for eachandevery in eachevery:
                    if eachandevery is not '.' and (int(eachandevery) == int(each)):
                        eachevery[i] = '.'
                    i+=1
                    ans = win()
                    if ans[0] == 1:
                        return (each,ans[1])

value,board = main()
ans = 0

for each in boards[board]:
    for every in each:
        if every is not '.':
            ans += int(every)

print(ans)
print(value)
print(ans * value)
