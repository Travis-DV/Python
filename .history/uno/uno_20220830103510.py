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
        normalcolorsoptions = ["red", "blue", "green", "yellow", "red", "blue", "green", "yellow", "wild"]
        normcolors = ["red", "blue", "green", "yellow"]
        normalcards = "0,1,2,3,4,5,6,7,8,9".split(",") + ["skip", "reverse", "+2"]
        normalwilds = ["wild", "+4"]
        color = r.choice(normalcolorsoptions)
        if color in normcolors:
            
        newnormalcard = {}

newplayer = player()
newplayer.addcard()