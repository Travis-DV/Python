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
        normalstuff = {"colors": ["red", "blue", "green", "yellow", "red", "blue", "green", "yellow", "special"], "numbers": "0,1,2,3,4,5,6,7,8,9".split(",") + ["skip", "reverse", "+2"], "special": ["wild", "+4", "flip"]}
        color = r.choice(normalstuff["colors"])
        if color != "special":
            number = r.choice(normalstuff["numbers"])
        elif color == "special":
            number = r.choice(normalstuff["wilds"])
        self.normalcards += {"color": color, "number": number}
        #FLIP
        flipstuff = {"colors": ["purple", "teal", "orange", "pink", "purple", "teal", "orange", "pink", "special"], "numbers": "0,1,2,3,4,5,6,7,8,9".split(",")}

newplayer = player()
newplayer.addcard()
print(newplayer.normalcards[0])