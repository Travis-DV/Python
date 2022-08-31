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
        normalstuff = {"colors": ["red", "blue", "green", "yellow", "red", "blue", "green", "yellow", "wild"], "numbers": "0,1,2,3,4,5,6,7,8,9".split(",") + ["skip", "reverse", "+2"], "wilds": ["wild", "+4"]}
        color = r.choice(normalstuff["colors"])
        if color != "wild":
            number = r.choice(normalstuff["numbers"])
        elif color == "wild":
            number = r.choice(normalstuff["wilds"])
        self.normalcards += {"color": color, "number": number}
        #FLIP
        flipstuff

newplayer = player()
newplayer.addcard()
print(newplayer.normalcards[0])