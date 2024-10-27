file = open("TestCase.in", "r")

lineLength = int(file.readline())
cowLine = []

minimumIndex = 0
currentIndex = 0
currentChain = 0
numberOfDays = 0
smallestChain = lineLength

numberOfChains = 0

currentChar = file.read(1)
while currentChar == "0" or currentChar == "1":
    cowLine.append(int(currentChar))
    currentChar = file.read(1)

for i in range(lineLength):
    if cowLine[i] == 1:
        if currentChain == 0:
            currentIndex = i
        currentChain += 1

    if cowLine[i] == 0:
        if currentChain < smallestChain and i != 0 and cowLine[i-1] == 1:
            smallestChain = currentChain
            minimumIndex = currentIndex

        if i != 0 and cowLine[i-1] == 1:
            currentChain = 0
            numberOfChains += 1

    if cowLine[i] == 1 and i == lineLength - 1:
        if currentChain < smallestChain:
            smallestChain = currentChain
            minimumIndex = currentIndex
            numberOfChains += 1

if smallestChain % 2 == 1:
    numberOfDays = (smallestChain - 1) / 2
elif smallestChain == 2 and minimumIndex == lineLength - 2:
    numberOfDays = 1
elif smallestChain % 2 == 0:
    numberOfDays = (smallestChain) / 2 - 1

currentChain = 0
# for i in range(lineLength):
#     if cowLine[i] == 1:
#         currentChain += 1
#
#     if cowLine[i] == 0 or i == lineLength - 1:
#         if currentChain != 0:
            
