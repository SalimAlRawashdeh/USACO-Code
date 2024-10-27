from BessieCannonball.Line import Line
from BessieCannonball.Ball import Ball

file = open("TestCase.in", "r")
currentChar = file.read(1)
lineLength = ""
while currentChar != " ":
    lineLength = lineLength + currentChar
    currentChar = file.read(1)

lineLength = int(lineLength)
initialBallIndex = int(file.readline()) - 1

mainLine = Line(lineLength, initialBallIndex)

for i in range(lineLength):
    currentChar = file.read(1)
    tempVar = ""
    while currentChar != " ":
        tempVar = tempVar + currentChar
        currentChar = file.read(1)

    mainLine.addToList(tempVar, int(file.readline()))

mainBall = Ball(1)

while mainLine.isBallInLine() is True:
    result = mainLine.moveBall(mainBall)
    if result == "break":
        break

print(mainLine.getNumberOfBrokenTargets())
