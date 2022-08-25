import random as r



def makingboard():
    height, width = 10, 10
    cords = x, y = 0, 0
    board = []
    while (x <= height):
        board += []
        while (y <= width):
            rand = r.randint(1,2)
            if x == 0 or x == 10:
                board[x, y] == 3
            elif (y == 0 or y == 10):
                if (x == 1):
                    board[x, y] = rand
                    board[x+1, y] = rand
                elif (x == 9):
                    board[x, y] = rand
                    board[x-1, y] = rand
                else:
                    board[x, y] = 1
            else:
                board[x, y] = 0
            y += 1
        x += 1

def printboard(board):
    word = ""
    for x in board:
        for y in board[x]:
            if board[x, y] == 0:
                word += "  "
            elif board[x, y] == 1:
                word += "|"
            elif board[x, y] == 3:
                word += "~~"
            elif board[x, y] == 2:
                word += "#"
        word += "\n"
    print(word)

board = makingboard()
printboard(board)