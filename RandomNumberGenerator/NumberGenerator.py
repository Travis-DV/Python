from random import randint
print("How many digets?")
input1 = input()
inpS = input1
input1 = int(input1)
inpS = int(inpS)
scrnum = 0
counter = 0
while input1 > 0:
        ran= randint(1,9)
        if scrnum <= 0:
            scrnum= ran
        else:
            scrnum= scrnum * 10 + ran
        input1= input1-1
        counterint= round(inpS/10+0.1)
        if counter == counterint:
            print("Degits left: " + str(input1) + ", Num: " + str(scrnum))