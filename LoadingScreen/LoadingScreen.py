# -----------------------------------------------------------
#
#     Project:     Cool Loading screen
#    Author:       Travis Findley
#    Created:      11/15/2021
#    Description:  A Uselass but cool looking loading screen
# -----------------------------------------------------------

# Library imports

from random import randint
import time

# Starting verables

per = 0
times = []
ttime = 0
word = ""
lo = "Loading."
con = 0
done = 0
hc = 0
spc = "     "
toss = randint(1,2)

# Begin project code
while 100 > per:
    ran = randint(1,3)
    if 1 == ran or 0 == per:
        if per != 0:
            ran = randint(1,8)
            if ran == 1:
                per = (per/2)
                time.sleep(0.2)
                times.append(0.2)
                per = (per*3.07)
            elif ran == 2:
                ran = randint(1,180)/100
                time.sleep(ran)
                times.append(ran)
                per = per/2
            elif ran == 3:
                ran = randint(0, 9)
                ran = ran/10
                per = 99+ran
                ran = randint(1,80)/100
                time.sleep(ran)
                times.append(ran)
                per = 45
            elif ran == 4:
                ran = randint(1,45)
                per = per+ran
            else:
                ran = randint(1,4)
                per = per+ran
        else:
            per = randint(0,50)
    if 100 >= per:
        if con < 3:
            lo = lo+"."
        elif con == 3:
            lo = "Loading."
            con = 0
        else:
            print("error")
    else:
        lo = "Complete!!"
    con = con+1
    per = round(per)
    if per > 100:
        per = 100
    pers = per-1
    perh = 100-per
    lefto = ""
    word = "["
    if 1 == toss:
        while 0 < pers:
            pers = pers-1
            word = word + "#"
        while 0 < perh:
            lefto = lefto + " "
            perh = perh-1
        word = word+"#"+lefto+"]"
    elif 2 == toss:
        while 0 < pers:
            word = word + "-"
            pers = pers-1
        while 0 < perh:
            lefto = lefto + " "
            perh = perh-1
        if 100 > per:
            word = word+">"+lefto+"]"
        else:
            word = word+"-]"
    while perh > 0:
        lefto = lefto + " "
        perh = perh-1
    per = str(per)
    print(lo + spc + per + "%")
    per = int(per)
    print(word)
    ran = randint(1,30)/100
    time.sleep(ran)
    times.append(ran)