import os
from random import randint
import loading
#loading
print("Do you want to play the guessing game? Y, N")
input1= input()
yes= ["Y", "y"]
scrnum= 0
win= 0
#do you want to play?
if input1 in yes:
    print("One or Two Players; 1,2.")
    input1= int(input())
#If single player
    if input1 == 1:
        print("Do you want to give Digits or 1-x? D or X")
        input1= input()
        if input1 == "D" or input1 == "d":
            print("How many Digits do you want?")
            input1= int(input())
            Guesses= round(input1 + input1*1.50)
        #making the number
            while input1 > 0:
                ran= randint(1,9)
                if scrnum <= 0:
                    scrnum= ran
                else:
                    scrnum= scrnum * 10 + ran
                input1= input1-1
        elif input1 == "X" or input1 == "x":
            print("What number cap do you want?")
            input1= int(input())
            scrnum= randint(1,input1)
            #number of guesses
            rep= 0
            while round(input1) > 0:
                input1 = input1/10
                rep= rep+1
            Guesses= round(rep + rep*1.50)
    #W/ friend
    elif input1 == 2:
        print("Have your friend input in a number")
        scrnum= int(input())
        print("Enter how many guesses they should have")
        Guesses= int(input())
        os.system('clr')
        win= 0
    #actual game
    while win != 1 and Guesses >= 0:
        if Guesses != 0:
            GuessesSTR= str(Guesses)
            print("You have " + GuessesSTR + " Guesses left!!")
            print("What do you want to guess?")
            mrg= int(input())
            if mrg == scrnum:
                Guesses= Guesses-1
                GuessesSTR= str(Guesses)
                print("You WIN, you had " + GuessesSTR + " Guesses left")
                win= 1
            else:
                if mrg > scrnum:
                    print("you need to guess lower")
                    Guesses= Guesses - 1
                    GuessesSTR= str(Guesses)
                elif mrg < scrnum:
                    print("You need to Guess higher")
                    Guesses= Guesses - 1
                    GuessesSTR= str(Guesses)
        else:
            print(scrnum)
            Guesses= Guesses-1