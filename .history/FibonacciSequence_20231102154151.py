def fibonacci(startnum):
    sequence = [0, 1]
    if startnum != "no":
        intamount = startnum
        if intamount < 0:
            return -1
    else:
        user_input = input("How many numbers do you want?\n")
        while True:
            try:
                return int(user_input)
            except:
                user_input = input("Numbers only please\n")
    for int in range(intamount):
        sequence.append(sequence[-2] + sequence[-1])
    while True:
        amount = input(f"Do you want to see the whole sequence or just the one at the index {intamount} (the number you provided earlier)? [all, index]\n)")
    
        if amount == "all":
            return ', '.join(map(str, sequence))
        elif amount == "index":
            return sequence[startnum]


print(f"{fibonacci()}")
