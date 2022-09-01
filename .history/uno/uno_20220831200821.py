#MOVE THIS INTO .NET AT HOME
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
        normalstuff = {"colors": ["red", "blue", "green", "yellow", "red", "blue", "green", "yellow", "special"], "numbers": [["0", 0],["1", 1],["2",1],["3",3],["4",4],["5",5],["6",6],["7",7],["8",8],["9",9]], "special": [["wild", 30], ["+4 wild", 50], ["flip", 60], ["+1", 10], ["skip", 20], ["reverce", 20]]}
        newcard = card()
        newcard.addcolor(False, normalcolor=r.choice(normalstuff["colors"]))
        if newcard.colors[0] != "special":
            newcard.addnumber(False, normalnumber=r.choice(normalstuff["numbers"][0]))
        elif newcard.colors[0] == "special":
            newcard.addnumber(False, normalnumber=r.choice(normalstuff["special"][0]))
        #FLIP
        flipstuff = {"colors": ["purple", "teal", "orange", "pink", "purple", "teal", "orange", "pink", "special"], "numbers": [["0", 0],["1", 1],["2",1],["3",3],["4",4],["5",5],["6",6],["7",7],["8",8],["9",9]], "special": [["wild", 30], ["+2 wild", 30], ["+5", 60], ["skip all", 20], ["flip", 60], ["draw to color", 40], ["skip", 20], ["reverce", 20]]}
        newcard.addcolor(True, flipcolor=r.choice(flipstuff["colors"]))
        if newcard.colors[1] != "special":
            newcard.addnumber(True, flipnumber=r.choice(flipstuff["numbers"][0]))
        elif newcard.colors[1] == "special":
            newcard.addnumber(True, flipnumber=r.choice(flipstuff["special"][0]))
        self.cards.append(newcard)
        #points
        self.points += normalstuff["points"][normalstuff["colors"].index(newcard.colors[0])] + flipstuff["points"][flipstuff["colors"].index(newcard.colors[1])]
        print(normalstuff["points"][0])

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

    def printstuff(self):
        print(f"You have a {self.colors[0]} {self.number[0]} on the normal side and on the flip side you have a {self.colors[1]} {self.number[1]}")

def isint(string):
    try:
        return int(string)
    except:
        return -1

def makeplayers():
    players = []
    amountofplayers = isint(input("How many players do you want to have? (max 4)\n"))
    while True:
        if amountofplayers > 1 and amountofplayers < 5:
            break
        amountofplayers = isint(input("Please input a number between 2 and 4\n"))
    for x in range(amountofplayers):
        players.append(player())
    return players

players = makeplayers()
players[0].addcard()
players[0].cards[-1].printstuff()
#print(players[0])