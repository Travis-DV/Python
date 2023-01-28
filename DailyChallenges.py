print("hello") #This is for day 1
print(f"20-6={20-6}")
print(f"20+25={20+25}")
print(f"57/31={57/31}")
print(f"42*76={42*76}")
print(f"int only: 24/5={int(24/5)}")
print(f"Remander only: 25/6={25%6}")
variable1 = "variable"
print(variable1)
numb1 = []
for numb in range(0, 101):
    if 0 <= numb:
        numb1.append(str(numb))
count = 0
word = numb1[count]
count = 1
while 100 >= count:
    word += " "
    word += numb1[count]
    count += 1
print(word)