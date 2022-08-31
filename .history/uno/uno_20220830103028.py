#MOVE THIS INTO .NET AT HOME

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
        normalcolors = ["red", "blue", "green", "yellow"]
        normalcards = "0123456789".split("") + ["skip", "reverse", "+2"]
        newnormalcard = {}
        word = ""
        for x in normalcards:
            word += x
            word += ", "
        print(word)

newplayer = player()
newplayer.addcard()