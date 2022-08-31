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
        normalcolors = ["red", "blue", "green", "yellow", "red", "blue", "green", "yellow", "wild"]
        normalcards = "0,1,2,3,4,5,6,7,8,9".split(",") + ["skip", "reverse", "+2"]
        normalwilds = ["wild", "+4"]
        r.randi
        newnormalcard = {}

newplayer = player()
newplayer.addcard()