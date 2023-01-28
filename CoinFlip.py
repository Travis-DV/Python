import random as r
playing = True
posib = ['heads', 'tails']

while playing:
    print(r.choice(posib))
    userinp = str.lower(input("Go again y, n\n"))
    if userinp == "y":
        playing == True
    elif userinp == "n":
        playing == False