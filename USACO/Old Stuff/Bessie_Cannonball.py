file = open("TestCase.in.in", "r")
currentChar = file.read(1)
lineLength = ""
while currentChar != " ":
    lineLength = lineLength + currentChar
    currentChar = file.read(1)

lineLength = int(lineLength)
currentIndex = int(file.readline()) - 1
attackPower = 1
numberOfTargets = 0

numberLine = [[0 for i in range(2)] for j in range(int(lineLength))]
damagedTargets = []
visitedPads = []

for i in range(len(numberLine)):
    currentChar = file.read(1)
    tempVar = ""
    while currentChar != " ":
        tempVar = tempVar + currentChar
        currentChar = file.read(1)

    numberLine[i][0] = int(tempVar)
    numberLine[i][1] = int(file.readline())

while 0 < currentIndex < lineLength - 1:
    flag = "false"

    for k in range(len(damagedTargets)):
        if currentIndex == damagedTargets[k]:
            flag = "true"

    if numberLine[currentIndex][0] == 1:
        if abs(attackPower) >= numberLine[currentIndex][1] and flag == "false":
            numberOfTargets += 1
            damagedTargets.append(currentIndex)
        currentIndex += attackPower

    else:
        if attackPower < 0:
            attackPower = -1 * attackPower
            attackPower += numberLine[currentIndex][1]
            visitedPads.append(currentIndex)
            currentIndex += attackPower
        else:
            attackPower += numberLine[currentIndex][1]
            attackPower = -1 * attackPower
            visitedPads.append(currentIndex)
            currentIndex += attackPower



        if len(visitedPads) >= 2:
            if numberLine[visitedPads[len(visitedPads) - 1]][1] == 0 and numberLine[visitedPads[len(visitedPads) - 2]][1] == 0:
                break


print(numberOfTargets)