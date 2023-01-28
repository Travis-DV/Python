import os, random as r
os.system("clear")

def oneplayer():
    while True:
        userinp = str.lower(input("Do you want to give amount of digets or 1-x? D, X\n"))
        if userinp == "d" or userinp == "x":
            break
        print("error")
    if userinp == "d":
        while True:
            userinp = str.lower(input("How many digets do you want?\n"))
            if userinp.isnumeric():
                guesses = round(int(userinp) + int(userinp)*1.50)
                secretnum = r.randint(1,(10*int(userinp)))
                break
            print("error")
    if userinp == "x":
        userinp = str.lower(input("What number cap do you want?\n"))
        if userinp.isnumeric():
            userinp = int(userinp)
            secretnum = r.randint(1,userinp)
            while round(userinp) > 0:
                userinp = userinp/10
                rep = rep+1
            guesses = round(rep + rep*1.50)
    print(f"You have {guesses} left")
    return guesses, secretnum

def twoplayer():
    while True:
        userinp = str.lower(input("Have a freind input a number.\n"))
        if userinp.isnumeric():
            secretnum = int(userinp)
            break
        print("error")
    while True:
        userinp = str.lower(input("Have a freind input amount of guesses.\n"))
        if userinp.isnumeric():
            guesses = int(userinp)
            break
        print("error")
    os.system("clear")
    return secretnum, guesses

def guessing(secretnum):
    win = False
    while True:
        userinp = str.lower(input("What do you want to guess?\n"))
        if userinp.isnumeric():
            userinp = int(userinp)
            break
        print("error")
    if secretnum > userinp:
        print("Guess higher")
    elif secretnum < userinp:
        print("Guess lower")
    elif secretnum == userinp:
        print("You Win!!!")
        win = True
    return win

def playing():

    win = False
    userinp = str.lower(input("How many players are playing? 1 or 2\n"))

    if userinp == "1":
        guesses, secretnum = oneplayer()
    elif userinp == "2":
        guesses, secretnum = twoplayer()

    while not win and guesses > 0:

        win = guessing(secretnum)
        guesses -= 1
        if guesses == 0 and not win:
            print(f"You lost :( the number was {secretnum}")

playing()
