import time
start_time = time.time()

def bubble_sort(inputList):
    done = False;
    topLevelIteration = len(inputList)-1;
    while not done:
        done = True
        
        for i in range(len(inputList)-1):
            if i == topLevelIteration:
                break
            s = f"{i} [{inputList[i]}, {inputList[i+1]}] ->"
            if (inputList[i] > inputList[i+1]):
                inputList[i], inputList[i+1] = inputList[i+1], inputList[i]
                done = False
            print(f"{s} [{inputList[i]}, {inputList[i+1]}]")
        print(f"{topLevelIteration} {inputList}\n")
        topLevelIteration -= 1
    print("Sorted array:", inputList)

arr = [1, 34, 54, 2, 5, 90]

def getInput():
    userInput = input("Input a list of numbers separated by commas:\n")
    splitInput = userInput.split(",")
    for i in splitInput:
        if i.isnumeric():
            arr.append(int(i))
        else:
            print(f"Invalid input: {i}")

#getInput()
print(f"Original array: {arr}")
bubble_sort(arr)

print("--- %s seconds ---" % (time.time() - start_time))