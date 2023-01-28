import time, os, random as r


def printper(per, load, Fullunf):
    os.system("clear")
    word = "error"
    if per >= 100:
        word = "Complete!!"
    elif per < 100:
        word = "Loading"
        for i in range(load):
            word += "."
        for i in range(5-load):
            word += "  "
        word += f"{per}%"
    print(word)
    #Actual bar
    word = "["
    for i in range(per):
        word += Fullunf[0]
        if i == 100: break
    if per < 100:
        word += Fullunf[1]
    for i in range(99-per):
        word += " "
    word += "]"
    print(word)

def loadd(load): #The player index loop
    if load == 3: return 1 #If it is on the last player set index to 0
    elif load < 3: return load + 1 #else return the index +1

def full():
    ran = r.randint(1,2)
    if ran == 1:
        Fullunf = ("#", " ")
    elif ran == 2:
        Fullunf = ("-", ">")
    return Fullunf

def perlogic(per):
    ran = r.randint(1,10)
    if ran == 1:
        per = (per//2)
        time.sleep(0.2)
        per = round(per*3.07)
        #print(f"one, {per}")
    elif ran == 2:
        time.sleep(r.randint(10,89)/100)
        per = per//2
        #print(f"two, {per}")
    elif ran == 3:
        per = 99+r.randint(0, 9)//10
        #print(f"three 1/2, {per}")
        time.sleep(r.randint(1,60)/100)
        per = 45
        print(f"three, {per}")
    elif ran == 4:
        per = per+r.randint(1,45)
        #print(f"four, {per}")
    else:
        per = per+r.randint(1,4)
    return per

def main():

    times = [time.time()]
    os.system("clear")
    persent = 1; load = 0
    Fullunf = full()

    while persent <= 100:
        if persent != 100: persent = perlogic(persent)
        elif persent <= 100: persent = 100

        printper(persent, load, Fullunf)
        load = loadd(load)

    times.append(time.time())
    print(f"It took {round(times[1]-times[0])} seconds")

main()