
class star:

    def __init__(self, name):
        yn = str.lower(input(f"Do you want to rename {name}: "))
        if yn == "y" or yn == "yes":
            self.name = input("What do you want to name it: ")
        else:
            self.name = name
        self.mass = misc.getintstr(f"What mass of the {self.name} (kg) (add a '?' to do scientific notation): ")
        self.diameter = misc.getintstr(f"What is thee diameter of the {self.name} (km): ")
        self.density = self.mass/((4/3)*3.14*((self.diameter/2)**3))
        print(self.density)


class planet:

    def __init__(self, name):
        yn = str.lower(input(f"Do you want to rename {name}: "))
        if yn == "y" or yn == "yes":
            self.name = input("What do you want to name it: ")
        else:
            self.name = name
        nummoons = misc.getintstr(f"How many moons do you want around {self.name}: ")
        numrings = misc.getintstr(f"How many rings do you want around {self.name}: ")
        print("-----------------------------------------------")
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
        print("##############################")
        numstars = misc.getintstr("How many stars do you want: ")
        numplanets = misc.getintstr("How many planets do you want: ")
        print("------------------------------")
        stars = []
        planets = []
        for int in range(numstars):
            stars.append(star(f"star {int+1}"))
        for int in range(numplanets):
            planets.append(planet(f"planet {int+1}"))

class misc:

    def getintstr(string):
        userinput = str.lower(input(string))
        while True:
            if userinput[0] == "?":
                return misc.scientificnotation(userinput)
            elif userinput != "" and userinput.isdigit() and int(userinput) >= 0:
                return int(userinput)
            userinput = str.lower(input("numbers <0 only please: "))

    def scientificnotation(string):
        string = string.replace("?", "")
        string = string.split("x")
        string[1] = string[1].replace("10^", "")
        string = float(string[0]) * (10**float(string[1]))
        return string
        
systems = []
systems.append(system())