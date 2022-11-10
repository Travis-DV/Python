
class star:

    def __init__(self):
        pass

class planet:

    def __init__(self, name):
        yn = str.lower(input(f"Do you want to rename {name}: "))
        if yn == "y" or yn == "yes":
            self.name = input("What do you want to name it: ")
        else:
            self.name = name
        nummoons = misc.getintstr(f"How many moons do you want on {self.name}: ")
        numrings = misc.getintstr(f"How many rings do you want around {self.name}: ")
        self.moons = []
        self.rings = []
        for int in range(nummoons):
            self.moons.append(moon())
        for int in range(numrings):
            self.rings.append(ring())

class moon:
    def __init__(self):
        pass

class ring:
    def __init__(self):
        pass

class system:

    def __init__(self):
        numstars = misc.getintstr("How many stars do you want: ")
        numplanets = misc.getintstr("How many planets do you want: ")
        print("------------------------------  ")
        stars = []
        planets = []
        for int in range(numstars):
            stars.append(star())
        for int in range(numplanets):
            planets.append(planet(f"planet {int+1}"))

class misc:
    def getintstr(string):
        userinput = str.lower(input(string))
        while True:
            if not userinput.isalpha() and int(userinput) > 0:
                return int(userinput)
            userinput = str.lower(input("numbers only please: "))
        
systems = []
systems.append(system())