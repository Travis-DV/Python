import random
board = [[random.randint(1,2),0,0,0,0,0,0,0,0,0,random.randint(1,2)], [1,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,3,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,1], [random.randint(1,2),0,0,0,0,0,0,0,0,0,random.randint(1,2)]]
board[1][0] = board[0][0]; board[1][10] = board[0][10]; board[9][0] = board[10][0]; board[9][10] = board[10][10]

word = ""
cp = []
error = "\033[1;31mError, try inputing again\033[1;0m"

def topbottem():
    global board, word
    for i in range(0,len(board[1])-1):
        word += "~~~"
    word += "\n"
    return word

def printboard():
    global board,topbottem, word, cp; index2 = -1; index3 = 0
    word = topbottem()
    for r in board:
        for i in board[index3]:
            if index2 < len(board[index3]):
                if i == 0:
                    word += "   "
                elif i == 1:
                    word += "|"
                elif i == 2:
                    word += "#"
                elif i == 3:
                    word += " P "
                    cp = [index3,index2+1]
            index2 += 1
        index2 = -1
        word += "\n"
        index3 += 1
    word = topbottem()
    word += "(Do you want to go UP DOWN LEFT RIGHT)\n"
    user_input = str.lower(input(word))
    return user_input, cp

user_input, cp = printboard()
while True:
    if "u" in user_input:
        if cp[0] > 0:
            board[cp[0]][cp[1]] = 0
            board[cp[0]-1][cp[1]] = 3
    elif "d" in user_input:
        if cp[0] < 10:
            board[cp[0]][cp[1]] = 0
            board[cp[0]+1][cp[1]] = 3
    elif "r" in user_input:
        if cp[1] < 9:
            board[cp[0]][cp[1]] = 0
            board[cp[0]][cp[1]+1] = 3
        elif board[cp[0]][cp[1]-1] == 2:
            print("cool")
    elif "l" in user_input:
        if cp[1] > 1:
            board[cp[0]][cp[1]] = 0
            board[cp[0]][cp[1]-1] = 3
        elif board[cp[0]][cp[1]-1] == 2:
            print("cool")
    else:
        print(error)
    word = ""
    user_input, cp = printboard()