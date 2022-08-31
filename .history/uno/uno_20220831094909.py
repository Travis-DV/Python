#MOVE THIS INTO .NET AT HOME

import imp


import random as r

class player:

    def __init__(self):

        self.normalcards = []
        self.flippedcards = []
        self.name = ""
        self.points = 0
        self.onuno = False
        #return self

    def addcard(self):
        #NORMAL
        normalstuff = {"colors": ["red", "blue", "green", "yellow", "red", "blue", "green", "yellow", "special"], "numbers": "0,1,2,3,4,5,6,7,8,9".split(",") + ["skip", "reverse", "+2"], "special": ["wild", "+4 wild", "flip", "+1", "skip", "reverce"], "points": [0,1,2,3,4,5,6,7,8,9,30,50,20,10,20,20]}
        color = r.choice(normalstuff["colors"])
        if color != "special":
            number = r.choice(normalstuff["numbers"])
        elif color == "special":
            number = r.choice(normalstuff["wilds"])
        self.normalcards += {"color": color, "number": number}
        #FLIP
        flipstuff = {"colors": ["purple", "teal", "orange", "pink", "purple", "teal", "orange", "pink", "special"], "numbers": "0,1,2,3,4,5,6,7,8,9".split(",") + ["wild", "+2 wild", "+5", "skip all", "flip", "draw to color", "skip", "reverce"], "points": [0,1,2,3,4,5,6,7,8,9,50,20,20,30,20,60,20,20]}

newplayer = player()
newplayer.addcard()
print(newplayer.normalcards[0])