import os, random, time, colorama as c

c.init()
os.system("clear")


def isnum(message):
    while True:
        userInput = str.lower(input(f"{message}\n"))
        if userInput.isnumeric(): 
            return int(userInput)
        print("error")

class DNA:

    T = c.Back.MAGENTA+c.Fore.BLACK+"T"+c.Style.RESET_ALL
    A = c.Back.RED+c.Fore.BLACK+"A"+c.Style.RESET_ALL
    G = c.Back.BLUE+c.Fore.BLACK+"G"+c.Style.RESET_ALL
    C = c.Back.GREEN+c.Fore.BLACK+"C"+c.Style.RESET_ALL
    dnaStyledLetters = [ T, A, G, C ]

    dna = [[],[]]

    lastSplit = 0

    def __init__(this, length):
        for i in range(length): 
            this.dna[0].append(random.choice(this.dnaStyledLetters))

        # for i in this.dna[0]:
        #     if i == this.T:
        #         this.dna[1].append(this.A)
        #     elif i == this.A:
        #         this.dna[1].append(this.T)
        #     elif i == this.G:
        #         this.dna[1].append(this.C)
        #     elif i == this.C:
        #         this.dna[1].append(this.G)

        this.fillHalf()

        print(this.ToString())

    def fillHalf(this):
        baseIndex = 0
        workingIndex = 0

        if this.dna[0] == []:
            baseIndex = 1
            workingIndex = 0
        elif this.dna[1] == []:
            baseIndex = 0
            workingIndex = 1

        for i in this.dna[baseIndex]:
            if i == this.T:
                this.dna[workingIndex].append(this.A)
            elif i == this.A:
                this.dna[workingIndex].append(this.T)
            elif i == this.G:
                this.dna[workingIndex].append(this.C)
            elif i == this.C:
                this.dna[workingIndex].append(this.G)

    def split(this):

        if this.lastSplit == 0:
            this.lastSplit = 1
        elif this.lastSplit == 1:
            this.lastSplit = 0


        return this.dna[this.lastSplit]

    #def __str__(this):
    def ToString(this):
        return f"{''.join(this.dna[0])}\n{''.join(this.dna[1])}"
    
class RNA:

    # RNA
    # U - A
    # G - C

    U = c.Back.YELLOW+c.Fore.BLACK+"U"+c.Style.RESET_ALL

    rna = []

    def __init__(this, dna):
        dnaHalf = dna.split()
        for i in dnaHalf:
            #print(i)
            if i == dna.T:
                this.rna.append(dna.A)
            elif i == dna.A:
                this.rna.append(this.U)
            elif i == dna.G:
                this.rna.append(dna.C)
            elif i == dna.C:
                this.rna.append(dna.G)
        print(this.ToString())

    def ToString(this):
        return f"{''.join(this.rna)}"

def main():
    length = isnum("How long of a sequence do you want?")
    dna = DNA(length)
    print()
    rna = RNA(dna)
    #dna.makeDNA()
    #dna.append(dupeDNA(dna, c.Back.GREEN+c.Fore.BLACK+"A"+c.Style.RESET_ALL, c.Back.MAGENTA+c.Fore.BLACK+"T"+c.Style.RESET_ALL))
    #for i in dna:
        #for j in i: print(j, end = "")
        #print()

    #rna = dupeDNA(dna[0], c.Back.GREEN+c.Fore.BLACK+"A"+c.Style.RESET_ALL, c.Back.YELLOW+c.Fore.BLACK+"U"+c.Style.RESET_ALL)
    #for i in rna: print(j, end = "")
    #print()

main()