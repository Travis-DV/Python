#MOVE THIS INTO .NET AT HOME

import imp


import random as r

class player:

    def __init__(self):

        self.cards = []
        self.name = ""
        self.points = 0
        self.onuno = False
        #return self

    def addcard(self):
        #NORMAL
        normalstuff = {"colors": ["red", "blue", "green", "yellow", "red", "blue", "green", "yellow", "special"], "numbers": "0,1,2,3,4,5,6,7,8,9".split(",") + ["skip", "reverse", "+2"], "special": ["wild", "+4 wild", "flip", "+1", "skip", "reverce"], "points": [0,1,2,3,4,5,6,7,8,9,30,50,20,10,20,20]}
        newcard = card()
        newcard.addcolor(False, normalnumber=r.choice(normalstuff["colors"]))
        if newcard.colors[0] != "special":
            newcard.addnumber(False, normalnumber=r.choice(normalstuff["numbers"]))
        elif newcard.colors[0] == "special":
            newcard.addnumber(False, normalnumber=r.choice(normalstuff["wilds"]))
        #FLIP
        flipstuff = {"colors": ["purple", "teal", "orange", "pink", "purple", "teal", "orange", "pink", "special"], "numbers": "0,1,2,3,4,5,6,7,8,9".split(",") + ["wild", "+2 wild", "+5", "skip all", "flip", "draw to color", "skip", "reverce"], "points": [0,1,2,3,4,5,6,7,8,9,50,20,20,30,20,60,20,20]}
        newcard.addcolor(True, flipcolor=r.choice(flipstuff["colors"]))
        if newcard.colors[1] != "special":
            newcard.addnumber(True, flipnumber=r.choice(flipstuff["numbers"]))
        elif newcard.colors[1] == "special":
            newcard.addnumber(True, flipnumber=r.choice(flipstuff["wilds"]))
        #points
        self.points += normalstuff["points"][normalstuff["colors"].indexof(newcard.colors[0])]

class card:

    def __init__(self):
        self.colors = ["", ""]
        self.number = [-1, -1]

    def addcolor(self, isfliped, normalcolor = "", flipcolor =""):
        if not isfliped:
            self.colors[0] = normalcolor
        elif isfliped:
            self.colors[1] = flipcolor

    def addnumber(self, isfliped, normalnumber = -1, flipnumber = -1):
        if not isfliped:
            self.number[0] = normalnumber
        elif isfliped:
            self.number[1] = flipnumber

newplayer = player()
newplayer.addcard()
print(newplayer.normalcards[0])