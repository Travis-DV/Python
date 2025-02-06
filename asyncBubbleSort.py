import asyncio
import time
start_time = time.time()


async def breaker(inputList):
        newList = []
        for i in range(len(inputList)-1):
            newList.append([inputList[i],inputList[i+1]])
        print(newList)

        # for i in newList:
        #     await checker(i)
        #     print(i)
        await asyncio.gather(*(checker(i) for i in newList))
        print(newList)

async def checker(inputList):
    print(inputList)
    if inputList[0] > inputList[1]:
        inputList[0], inputList[1] = inputList[1], inputList[0]
    yield inputList

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
asyncio.run(breaker(arr))

print("--- %s seconds ---" % (time.time() - start_time))