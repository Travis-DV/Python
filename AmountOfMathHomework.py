index2 =0
print("What questions?")
input = input()
spaces = input.split(" ")
index2 = 0
tally = 0
def subtrac(placehold):
    placehold = placehold.split("-")
    mathh0 = int(placehold[0])
    mathh1 = int(placehold[1])
    mathh = mathh1 - mathh0
    return mathh
while index2 < len(spaces):
    action = 0
    if "," not in spaces[index2] and "-" not in spaces[index2]:
        #single numbers
        action = 1
        tally = tally+1
        placehold = spaces[index2]
        spaces.remove(placehold)
    if "-" in spaces[index2] and "," not in spaces[index2]:
        #non-alpha ranges
        action = 1
        placehold = spaces[index2]
        spaces.remove(placehold)
        mathh = subtrac(placehold)
        tally = tally+mathh
    if ",e" in spaces[index2] or ",o" in spaces[index2]:
        action = 1
        placehold = spaces[index2]
        spaces.remove(placehold)
        placehold = placehold.split(",")
        placehold = placehold[0]
        mathh = subtrac(placehold)
        mathh = mathh/2
        tally = tally+mathh
    if ",a" in spaces[index2]:
        action = 1
        placehold = spaces[index2]
        spaces.remove(placehold)
        placehold = placehold.split(",")
        placehold = placehold[0]
        mathh = subtrac(placehold)
        tally = mathh+tally
    if 0 == action:
        index2 = index2+1
    if 0 != len(spaces):
        print(spaces, tally)
    else:
        print(tally)
index2 = 0