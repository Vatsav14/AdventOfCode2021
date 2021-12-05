with open("input.txt", "r") as file:
    data = file.readlines()

insertions = data[0].split(',')

def win(board):
    i = 0
    while i < 5:
        if board[i][0] == '.' and board[i][1] == '.' and board[i][2] == '.' and board[i][3] == '.' and board[i][4] == '.':
            return 1
        if board[0][i] == '.' and board[1][i] == '.' and board[2][i] == '.' and board[3][i] == '.' and board[4][i] == '.':
            return 1
        i += 1
    return 0

def insert(board, number):
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            if board[i][j] is not '.' and int(board[i][j]) is int(number):
                board[i][j] = '.'
            j += 1
        i += 1
            
boards = dict()
i = 2
num = 0
while i < len(data):
    temp = list()
    temp.append(data[i].split())
    temp.append(data[i+1].split())
    temp.append(data[i+2].split())
    temp.append(data[i+3].split())
    temp.append(data[i+4].split())
    boards[num] = temp
    num += 1
    i += 6

winners = set()
for each in range(len(boards)):
    winners.add(each)

def main():
    for each in insertions:
        for every in boards:
            insert(boards[every], each)
            if win(boards[every]) == 1 and every in winners:
                winners.remove(every)
            if len(winners) == 1:
                print(winners)
                return (winners, each)

winners, value = main()
print(value)
for each in winners:
    print(boards[each])
