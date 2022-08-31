import random as r



def makingboard():
    height, width = 10, 10
    cords = x, y = 0, 0
    board = []
    for x in range(height):
        board += []
        for y in range(width):
            if x == 0 or x == 10:
                board[x][y] == 1
            else:
                board[x][y] = 0

"""
4 = is door = #
else set to wall = 1
"""

def isdoor(doors):
    if doors[0]:
        board[0][0] = 4
        board[1][0] = 4
    if doors[1]:
        board[10][0] = 4
        board[11][0] = 4
    if doors[2]:
        board[0][10] = 4
        board[1][10] = 4
    if doors[3]:
        board[10][10] = 4
        board[11][10] = 4

"""
0 = empty = "  "
1 = wall = if at 0 or max cols = | else = ~
2 = player = p
3 = possible door, doors 1 = tl 2 = tr 3 = bl and 4 = br
"""

def printboard(board):
    word = ""
    for x in board:
        for y in board[x]:
            if board[x, y] == 0:
                word += "  "
            elif board[x, y] == 1:
                if x == 0 or x == 10:
                    word += "|"
                else:
                    word += "~"
            elif board[x, y] == 4:
                word += "#"
            elif board[x, y] == 2:
                word += "P"
        word += "\n"
    print(word)

board = makingboard()
isdoor([True, False, False, False])
printboard(board)