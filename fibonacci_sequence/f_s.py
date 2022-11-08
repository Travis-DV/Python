
class sequence:

    def __init__(self):
        self.sequence = [1, 1]
        self.intamount = self.findhowmany()
        
    def runnext(self):
        self.sequence.append(self.sequence[-2] + self.sequence[-1])
    
    def findhowmany(self):
        user_input = input("How many numbers do you want?\n")
        while True:
            try:
                return int(user_input)
            except:
                user_input = input("Numbers only please\n")
    
    def actualyrun(self):
        for int in range(self.intamount):
            self.runnext()
    
    def stringit(self):
        ssequence = self.sequence
        ssequence.remove(self.sequence[0])
        printsequence = f"{self.sequence[0]}"
        for int in ssequence:
            printsequence += f", {int}"
        return printsequence

    def main(self):
        self.actualyrun()
        print(self.stringit())


sf = sequence()