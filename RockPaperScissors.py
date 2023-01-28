import random
from random import randint
play= 0
win= 0
lose= 0
if play == 0:
    print("Do you want to play rock paper sizers? Y, N")
    input1= input()
if input1 == "y" or input1 == "Y":
    play= 1
elif input1 == "YY" or input1 == "yy":
    play= 2
else:
    print("Goodbye then")
while play == 1 or play == 2:
    tie= 0
    ran= randint(1,3)
    print("what do you want to do? Rock: 1, Paper: 2, or Scissors:3?")
    rps= input()
    rps= int(rps)
    if rps <= 0:
        print("Please do a positive number")
    else:
        if rps == 1 and ran == 3:
            print("YOU WIN!!!!, the enamy went Scissors")
            win= win+1
        elif rps == 2 and ran == 1:
            print("YOU WIN!!!, the enemy went Rock")
            win= win+1
        elif rps == 3 and ran == 2:
            print("YOU WIN!!!, the enemy went Paper")
            win= win+1
        elif rps == 3 and ran == 1:
            print("you lose, the enamy went Rock")
            lose= lose+1
        elif rps == 1 and ran == 2:
            print("you lose, the enamy went Paper")
            lose= lose+1
        elif rps == 2 and ran == 3:
            print("you lose, the enamy went Scissors")
            lose= lose+1
        elif ran == rps:
            print("you tied")
            tie= 1
        else:
            print("Error")
    if tie != 1:
        if win > 0 and lose > 0:
            wl= win/lose
        elif win > 0:
            wl= win
        elif lose > 0:
            wl= lose
        wl= str(wl)
        print("Your win lose ratio is: " + wl)
        if play != 2:
            print("Play again? Y, N")
            input1= input()
            if input1 == "n" or input1 == "N":
                play= 0
            elif input1 == "Y" or input1 == "y":
                play= 1
            elif input1 == "YY" or input1 == "yy":
                play= 2
            elif input1 != "Y" or input1 != "y":
                print("Invaled input: " + input1)
