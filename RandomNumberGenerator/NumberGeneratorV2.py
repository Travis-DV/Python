import random as r, time, os

def main():
    times = [time.time()]
    num = 0
    while True:
        userinp = str.lower(input("How many ditgets do you want?\n"))
        if userinp.isnumeric(): userinp = int(userinp); break
        print("error")
    while True:
        sleep = str.lower(input("How long a break do you want? (/100)\n"))
        if sleep.isnumeric(): sleep = int(sleep)/100; break
        print("error")
    for i in range(userinp):
        num *= 10
        num += r.randint(1,9)
        print(print(f"{num}\nYou have {userinp - i} ditgets left"))
        time.sleep(sleep)
        os.system("clear")
    times.append(time.time())
    print(f"It took {round(times[1]-times[0])} seconds\nYour final number was {num}")


main()