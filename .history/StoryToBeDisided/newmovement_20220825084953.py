import random as r

"""
0 = empty = "  "
1 = wall = if at 0 or max cols = | else = ~
2 = player = p
3 = possible door, doors 1 = tl 2 = tr 3 = bl and 4 = br
"""

def makingboard():
    height, width = 10, 10
    cords = x, y = 0, 0
    board = []
    for x in range(height):
        board += []
        while (y <= width):
            rand = r.randint(1,2)
            if x == 0 or x == 10:
                board[cords] == 1
            else:
                board[cords] = 0
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