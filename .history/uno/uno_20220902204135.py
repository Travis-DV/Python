#MOVE THIS INTO .NET AT HOME
from dis import dis
import random as r

class player:

    def __init__(self):

        self.cards = []
        self.name = ""
        self.points = 0
        self.onuno = False
        self.filloutcards()
        #return self

    def addcard(self):
        #NORMAL
        normalstuff = {"colors": ["red", "blue", "green", "yellow", "red", "blue", "green", "yellow", "special"], "numbers": [["0", 0],["1", 1],["2",1],["3",3],["4",4],["5",5],["6",6],["7",7],["8",8],["9",9], ["flip", 60], ["+1", 10], ["skip", 20], ["reverce", 20]], "special": [["wild", 30], ["+4 wild", 50]]}
        cards = card()
        cards.addcolor(False, normalcolor=r.choice(normalstuff["colors"]))
        if cards.colors[0] != "special":
            temp = r.choice(normalstuff["numbers"])
            cards.addnumber(False, normalnumber=temp[0])
        elif cards.colors[0] == "special":
            temp = r.choice(normalstuff["special"])
            cards.addnumber(False, normalnumber=temp[0])
        self.points += temp[1]
        #FLIP
        flipstuff = {"colors": ["purple", "teal", "orange", "pink", "purple", "teal", "orange", "pink", "special"], "numbers": [["0", 0],["1", 1],["2",1],["3",3],["4",4],["5",5],["6",6],["7",7],["8",8],["9",9],["+5", 60], ["skip all", 20], ["flip", 60], ["draw to color", 40], ["skip", 20], ["reverce", 20]], "special": [["wild", 30], ["+2 wild", 30]]}
        cards.addcolor(True, flipcolor=r.choice(flipstuff["colors"]))
        if cards.colors[1] != "special":
            temp = r.choice(flipstuff["numbers"])
            cards.addnumber(True, flipnumber=temp[0])
        elif cards.colors[1] == "special":
            temp = r.choice(flipstuff["special"])
            cards.addnumber(True, flipnumber=temp[0])
        self.points += temp[1]
        self.cards.append(cards)

    def filloutcards(self):
        for i in range(7):
            self.addcard()

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

class discardpile(player):

    def __init__(self):
        self.cards = card()

    def getstartingcard(self):
        while True:
            self.cards = self.addcard()
            if not "special" in self.cards.colors:
                break

    def isitelegable(self, card, isfliped):
        if isfliped and (card.colors[1] == self.cards.colors[1] or card.colors[1] == "special" or card.number[1] == self.cards.number[1]): return True
        elif not isfliped and (card.colors[0] == self.cards[0] or card.colors[0] == "special" or card.number[0] == self.cards.number[0]): return True
        else: return False

    def replacecard(self, cards, isfliped):
        if self.isitelegable(cards, isfliped):
            self.topcard = cards

class gamelogic():

    def __init__(self):
        self.players = [player()]
        self.makeplayers()
        self.discardpile = discardpile()

    def isint(self, string):
        try: return int(string)
        except: return -1

    def getamountofplayers(self):
        amountofplayers = self.isint(input("How many players do you want to have? (max 4)\n"))
        self.players[0].name = input("What is your name?\n")
        while True:
            if amountofplayers > 1 and amountofplayers < 5:
                return amountofplayers - 1
            amountofplayers = self.isint(input("Please input a number between 2 and 4\n"))

    def makeplayers(self):
        amountofplayers = self.getamountofplayers()
        for x in range(amountofplayers):
            self.players.append(AI())
        return self.players

class AI(player):

    def __init__(self):
        self.name = r.choice(["Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia", "Evelyn", "Harper", "Luna", "Camila", "Gianna", "Elizabeth", "Eleanor", "Ella", "Abigail", "Sofia", "Avery", "Scarlett", "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Theodore", "Jack", "Levi", "Alexander", "Jackson", "Mateo", "Daniel", "Michael", "Mason", "Sebastian", "Ethan"])



game = gamelogic()