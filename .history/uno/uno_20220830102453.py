#MOVE THIS INTO .NET AT HOME

class player:

    def __init__(self):

        self.cards = []
        self.name = ""
        self.points = 0
        self.onuno = False
        return self

    def addcard(self):
        colors = ["red", "blue", "green", "yellow"]
        cards = "0123456789".list() + ["skip", "reverse", ""]
        newcard = {}