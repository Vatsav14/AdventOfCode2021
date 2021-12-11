with open("input.txt", "r") as file:
    data = [x.split() for x in file.readlines()]

coord = list()
for each in data:
    coord.append([(each[0].split(',')[0],each[0].split(',')[1]), \
                  (each[2].split(',')[0],each[2].split(',')[1])])

board = list()
for each in range(1000):
    board.append([0] * 1000)

def part1():
    for each in coord:
        if int(each[0][0]) == int(each[1][0]):
            y1, y2 = int(each[0][1]), int(each[1][1])
            if y2 < y1:
                y2, y1 = y1, y2
            while(y1 <= y2):
                board[int(each[0][0])][y1] += 1
                y1 += 1
            
        elif int(each[0][1]) == int(each[1][1]):
            x1, x2 = int(each[0][0]), int(each[1][0])
            if x2 < x1:
                x2, x1 = x1, x2
            while(x1 <= x2):
                board[x1][int(each[0][1])] += 1
                x1 += 1

        elif abs(int(each[0][0]) - int(each[1][0])) == abs(int(each[0][1]) - int(each[1][1])):
            x1, x2, y1, y2 = int(each[0][0]), int(each[1][0]), int(each[0][1]), int(each[1][1])
            if x1 < x2:
                x = 1
            else:
                x = -1
            if y1 < y2:
                y = 1
            else:
                y = -1
            while x1 - x2 != 0:
                board[x1][y1] += 1
                x1 += x
                y1 += y
            # To make sure the last point is also accounted for
            board[x1][y1] += 1
        
part1()


total = 0
for each in board:
    for element in each:
        if element > 1:
            total += 1

print(total)
