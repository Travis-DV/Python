import os, random as r, time as t, colorama as c

c.init()
os.system("clear")


def isnum(msg):
    while True:
        userinp = str.lower(input(f"{msg}\n"))
        if userinp.isnumeric(): userinp = int(userinp); break
        print("error")
    return userinp

def makeDNA():
    length = isnum("How long of a sequence do you want?")
    pdna = [c.Back.MAGENTA+c.Fore.BLACK+"T"+c.Style.RESET_ALL,
    c.Back.GREEN+c.Fore.BLACK+"A"+c.Style.RESET_ALL,
    c.Back.BLUE+c.Fore.BLACK+"G"+c.Style.RESET_ALL,
    c.Back.RED+c.Fore.BLACK+"C"+c.Style.RESET_ALL]
    dna = [[],[]]
    for i in range(length): dna[0].append(r.choice(pdna))
    return dna

def dupeDNA(dna, ais, aEquals):
    pdna = [c.Back.MAGENTA+c.Fore.BLACK+"T"+c.Style.RESET_ALL,
    c.Back.GREEN+c.Fore.BLACK+"A"+c.Style.RESET_ALL,
    c.Back.BLUE+c.Fore.BLACK+"G"+c.Style.RESET_ALL,
    c.Back.RED+c.Fore.BLACK+"C"+c.Style.RESET_ALL]
    ndna = []
    for i in dna:
        if i == pdna[0]:
            ndna.append(pdna[1])
        elif i == ais:
            ndna.append(aEquals)
        elif i == pdna[2]:
            ndna.append(pdna[3])
        elif i == pdna[3]:
            ndna.append(pdna[2])
    return ndna

def main():
    dna = makeDNA()
    dna.append(dupeDNA(dna, c.Back.GREEN+c.Fore.BLACK+"A"+c.Style.RESET_ALL, c.Back.MAGENTA+c.Fore.BLACK+"T"+c.Style.RESET_ALL))
    for i in dna:
        for j in i: print(j, end = "")
        print()
    rna = dupeDNA(dna[0], c.Back.GREEN+c.Fore.BLACK+"A"+c.Style.RESET_ALL, c.Back.YELLOW+c.Fore.BLACK+"U"+c.Style.RESET_ALL)
    for i in rna: print(j, end = "")
    print()

main()